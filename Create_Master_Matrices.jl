
using DataFrames

############################
# input
folder="C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\"

# abs seqs
#folder="C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\"

# noabs seqs
#folder="C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\"

############################
function compare_pairwise(species_seqs::Matrix{Int})
    num_seqs = size(species_seqs,1)  # count the number of sequences
    if(num_seqs < 2) # return an empty state if there is only one sequence
        return(DataFrame(seq1 = -1, seq2 = -1, length_seq1 = -1, length_seq2 = -1, overlap = -1., commons = -1, num_per_bp = -1.))
    end

    #Preinitialize containers
    seq1 = Int[]
    seq2 = Int[]
    length_seq1 = Int[]
    length_seq2 = Int[]
    overlap = Float64[]
    commons = Int[]
    num_per_bp = Float64[]
    for iter = 1:(num_seqs-1)
        for iter_sub = (iter + 1):num_seqs # For each pairwise combination of sequences
            pair_seqs = species_seqs[[iter, iter_sub], :]
            common_sites = minimum(pair_seqs, 1) .> 0 #Ensure that only sites existing in both sequences are compared (i.e. ignore loci missing from the alignment)
            if sum(common_sites) == 0.
                push!(num_per_bp, 0.)
            else
                trans = Bool[]
                for i in common_sites
                    trans = append!(trans,i)
                end
                num_segregating = sum(diff(pair_seqs[:, trans], 1) .!= 0)
                push!(num_per_bp, num_segregating/sum(common_sites))
            end
            push!(seq1, iter)
            push!(seq2, iter_sub)
            ls1 = sum(species_seqs[iter, :] .!= 0)
            ls2 = sum(species_seqs[iter_sub, :] .!= 0)
            push!(length_seq1, ls1)
            push!(length_seq2, ls2)
            push!(overlap, sum(common_sites)/max(ls1, ls2))  #Compute the overlap between the sequences
            push!(commons, sum(common_sites))
        end
    end
    DataFrame(seq1 = seq1, seq2 = seq2, length_seq1 = length_seq1, length_seq2 = length_seq2, overlap = overlap, commons = commons, num_per_bp = num_per_bp)
end

function create_master_matrices(foldername::String)
    species_list = [x[1:(end-6)] for x in filter(st->contains(st, ".fasta"), readdir(foldername))]      #identify unique file names ignoring the extension
    num_files = size(species_list,1)

    equalarea = latbands = biomes = anthromes = gridcells  = order = pop = DataFrame(species = String[], cell = String[], seq1 = Int[], seq2 = Int[], length_seq1 = Int[], length_seq2 = Int[], overlap = Float64[], commons = Int[], num_per_bp = Float64[])   # Pre-initialize the DataFrame to ensure correct element types

    for iter_file = 1:num_files
        # read in the sequence data for one species
        file_name_seq = joinpath(foldername, species_list[iter_file] * ".fasta")
        species_seqs = readdlm(file_name_seq, ',',Int)
        length_seq = size(species_seqs,2)

        # read the coordinates for one species
        file_name_coords = joinpath(foldername, species_list[iter_file] * ".coords")
        species_coords = readdlm(file_name_coords, ',')

        #GRID CELLS
        #apply a 4x4 lat-long degree grid to the coordinates
        coords_grid = hcat(ceil(Int, (species_coords[:,1] + 2) ./ 4) .* 4 .- 4, ceil(Int, species_coords[:,2] ./ 4) .* 4 .- 2)

        #calculate the summary statistic for each grid cell
        sitenames = mapslices(x -> "$(x[1])_$(x[2])", coords_grid, 2)
        gridcells = vcat(gridcells, calcspecies(species_list[iter_file], species_seqs, sitenames))

        #ANTHROMES
        file_name_anthrome = joinpath(foldername,"anthromes",species_list[iter_file] * ".coords")
        anthro = floor(Int, readdlm(file_name_anthrome)[:,3])
        # calculate the summary statistic for each grid cell
        anthromes = vcat(anthromes, calcspecies(species_list[iter_file], species_seqs, anthro))

        #BIOMES
        file_name_biome = joinpath(foldername,"biomes",species_list[iter_file] * ".coords")
        bio = floor(Int, readdlm(file_name_biome)[:,3])
        biomes = vcat(biomes, calcspecies(species_list[iter_file], species_seqs, bio))

        #LATITUDINAL BANDS
        latband = 10 * floor(Int,species_coords[:,1]/10)
        latbands = vcat(latbands, calcspecies(species_list[iter_file], species_seqs, latband))

        #EQUAL AREA GRID CELLS
        file_name_equal = joinpath(foldername,"equalarea",species_list[iter_file] * ".coords")
        equ = floor(Int, readdlm(file_name_equal)[:,3])
        equ = [String("$a") for a in equ]
        equalarea = vcat(equalarea, calcspecies(String(species_list[iter_file]), species_seqs, equ))
        println(iter_file)

        #iucn
        #file_name_iucn = joinpath(foldername,"iucn",species_list[iter_file] * ".coords")
        #iuc = floor(Int, readdlm(file_name_iucn)[:,3])
        #iucn = vcat(iucn, calcspecies(species_list[iter_file], species_seqs, iuc))

        #order
        file_name_order = joinpath(foldername,"order",species_list[iter_file] * ".coords")
        ord = floor(Int, readdlm(file_name_order)[:,3])
        order = vcat(order, calcspecies(species_list[iter_file], species_seqs, ord))

        #species
        #file_name_species = joinpath(foldername,"species",species_list[iter_file] * ".coords")
        #spe = floor(Int, readdlm(file_name_species)[:,3])
        #species = vcat(species, calcspecies(species_list[iter_file], species_seqs, spe))

        #population
        file_name_pop = joinpath(foldername,"populations",species_list[iter_file] * ".coords")
        po = floor(Int, readdlm(file_name_pop)[:,3])
        pop = vcat(pop, calcspecies(species_list[iter_file], species_seqs, po))


    end
    writetable("pairwise_gridcells_terrestrial_mammals.csv", gridcells)
    writetable("pairwise_anthromes_terrestrial_mammals.csv", anthromes)
    writetable("pairwise_biomes_terrestrial_mammals.csv", biomes)
    writetable("pairwise_latbands_terrestrial_mammals.csv", latbands)
    writetable("pairwise_equalarea_terrestrial_mammals.csv", equalarea)
    #writetable("pairwise_iucn_terrestrial_mammals.csv", iucn)
    writetable("pairwise_order_terrestrial_mammals.csv", order)
    #writetable("pairwise_species_terrestrial_mammals.csv", species)
    writetable("pairwise_population_terrestrial_mammals.csv", pop)

end

function calcspecies(species, species_seqs, sitenames)
    res = DataFrame(species = String[], cell = String[], seq1 = Int[], seq2 = Int[], length_seq1 = Int[], length_seq2 = Int[], overlap = Float64[], commons = Int[], num_per_bp = Float64[])
    uniq_grid = unique(sitenames, 1)
    println(uniq_grid)
    for iter_grid = 1:size(uniq_grid,1) # Go through each site in turn
        seqs_grid = species_seqs[findin(sitenames, uniq_grid[iter_grid, :]), :]   #find seqs

        tot_muts = compare_pairwise(seqs_grid)
        lns = size(tot_muts, 1)

        sp = []
        ce = []
        for i in 1:lns
            sp = append!(sp,[species])
            ce = append!(ce,vec(uniq_grid[iter_grid, :]))
        end
        println(sp,ce)
        tmp = DataFrame(species = sp, cell = ce )
        tot_muts = hcat(tmp, tot_muts)
        res = vcat(res, tot_muts)
    end

    for sym in [:seq1, :seq2, :length_seq1, :length_seq2, :overlap, :commons, :num_per_bp]
        res[sym][res[sym] .< 0.] = NA   #Replace empty values with an NA identifier
    end
    res
end

create_master_matrices(folder)
