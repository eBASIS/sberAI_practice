# Docker scripts
Here are some scripts that can make using this project easier.

Install, buid and run Docker container:

```bash 
bash install_docker.sh # (Re)install Docker
bash build_docker.sh # Build Docker container:
bash run_docker.sh # Run Docker container
```
**Note:** this container has access to a folder: `workspace`

You can access the running container:
```bash
bash into_docker.sh
```

Also you can install python requirements without docker:
 ```bash
 pip install -r requirements.txt
 ```

Also you should pull and run [Allenai SPV2](https://github.com/allenai/spv2) **docker** image:
```bash
docker pull allenai/spv2:2.10
docker run -p 8081:8081 allenai/spv2:2.10
```