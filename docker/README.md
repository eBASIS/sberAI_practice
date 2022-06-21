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

Also you should pull and run [Grobid](https://github.com/kermitt2/grobid) **docker** image:
```bash
docker pull grobid/grobid:0.7.1
docker run -t --rm --init -p 8070:8070 grobid/grobid:0.7.1
```
If you are able to use GPU, follow this:
```bash
docker run --rm --gpus '"device=1,2"' --init -p 8070:8070 grobid/grobid:0.7.1
```