# stress-mem

[Dockerhub](https://github.com/ar2pi/stress-mem)

A simple container to stress test memory.

## Build

```sh
docker build -t ar2pi/stress-mem .
```

## Run

```sh
docker run -it --rm --memory=128m --memory-swap=128m ar2pi/stress-mem
```

## Push

```sh
docker push ar2pi/stress-mem
```
