# Build

## Exectue build process localy

The build step is a pipeline decribe in ```Jenkinsfile```.

The step a runned in order with all bash script as [number]_[script_name].sh

Exemple, run one by one :
```bash
./0_fetch-dependencies.sh
./1_lint.sh (opt)
./3_build-prod.sh
./5_make_release.sh
./6_make_docker.sh
```

Now you can the docker you build with ```../test-prod/README.md```

If an error occur, use the ```99_clean.sh``` to clean all and revert rigths.

## Advanced

### Use nexus

To use nexus.alkante.alto get composer and/or npm package, you need to uncomment lines with NEXUS, NEXUS_USR and NEXUS_PSW in file:
- ./0_fetch-dependencies.sh
- ./Jenkinsfile

### Run assetic

To run assetic, you need to uncomment "Make asset cache" step in :
- ./Jenkinsfile