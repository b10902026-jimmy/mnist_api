sudo docker rm -f pytest
sudo docker run --name pytest -itd -v $PWD/.:/app test:1.0