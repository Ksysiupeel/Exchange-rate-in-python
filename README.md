[![Ksysiupeel](https://badgen.net/badge/Developer/Ksysiupeel/blue?icon=github)](https://github.com/ksysiupeel/) 

# Exchange_rate
This program uses the api https://exchangeratesapi.io/.

## Instalation
```cmd
pip install git+https://github.com/Ksysiupeel/Exchange-rate-in-python.git
```

## Usage
You how to import exchange_rate module
```python
from exchange_rate import Exchange_rate
```
Then you need to create a new instance
```python
show_currency = Exchange_rate("CURRENCY_SHORTCUT"") 
```

Now all you need to do is use the get() method
```python
show_currency.get()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)