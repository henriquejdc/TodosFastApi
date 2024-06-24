# fastapi_simple
Projeto simples de fastapi de CEPs


**No terminal:**
```
python3 -m venv venv
source venv/bin/activate
```


**Na venv ativa:**
```
pip install -r requirements.txt 
```

**Mongo:**
Necessário criar um database no mongo cloud e trocar na .env os dados
```
python -m pip install "pymongo[srv]"==3.6
```

**Iniciar:**
```
uvicorn main:app --reload
python main.py --reload
```


**Testes Unitários:**
``` 
ENV_MODE='test' pytest tests/
```
# TodosFastApi
