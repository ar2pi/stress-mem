# stress-mem

[Dockerhub](https://hub.docker.com/repository/docker/ar2pi/stress-mem)

A simple container to stress test memory.

## Run

```sh
docker run -it --rm --memory=128m --memory-swap=128m ar2pi/stress-mem
```

## Build

```sh
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t ar2pi/stress-mem \
  --push .
```

## @TODO:

- [ ] make configurable memory increment step and wait time
