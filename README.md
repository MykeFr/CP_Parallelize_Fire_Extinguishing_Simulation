# Concurrency and Parallelism 2021-22

### Agent-based Simulation of Fire Extinguishing

EduHPC 2019: Peachy assignment

(c) 2019 Arturo Gonzalez-Escribano, Jorge Fernandez-Fabeiro
Group Trasgo, Universidad de Valladolid (Spain)

--------------------------------------------------------------

    Group Id: G24
    Member 1: Tiago Cristina Mendes (55105)
    Member 2: Miguel Elias de Sousa França (55622)
    Member 3: Diogo Nuno da Gama Brás (55722)

--------------------------------------------------------------

How to compile this program:
--------------------------------------------------------------

    make extinguishing_seq  #Build only the sequential version"
    make extinguishing_impSeq  #Build only the improved sequential version"
    make extinguishing_omp   #Build only the OpenMP version"
    make extinguishing_flattened   #Build only the OpenMP version"
    
    make all #Build all versions (Sequential, OpenMP)"
    make debug   #Build all version with demo output for small surfaces)"
    make clean   #Remove targets"

    # Run the profiler
    gprof -b -l (extinguishing_seq | extinguishing_omp) gmon.out

--------------------------------------------------------------

How to run the examples:
--------------------------------------------------------------

    extinguishing_seq |extinguishing_impSeq | extinguishing_omp <config_file> | <command_line_args>
    <config_file> ::= -f <file_name>
    <command_line_args> ::= <rows> <columns> <maxIter> <numTeams> [ <teamX> <teamY> <teamType> ... ] <numFocalPoints> [ <focalX> <focalY> <focalStart> <focalTemperature> ... ]

--------------------------------------------------------------
