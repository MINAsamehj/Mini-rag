# mini-rag project

project to have a conversation with AI

## requirments
(can all be installed using conda)
1-python 3.10


## installation
### install the required packges
```bash
$ pip intall -r requirements.txt
```

### setup the environmet variables 

```bash
$ cp .env.example .env
```

and then setup the envirinment variables like `OPENAI_API_KEY`

### run the fastapi server

```bash
main:app --reload --host 0.0.0.0 --port 5000
```
