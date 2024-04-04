import logging

logging.basicConfig(filename='sims.log', level=logging.ERROR)
def logging_decorator(func):

   def wrapper(*args, **kwargs):
       try:

           result = func(*args, **kwargs)

           return result

       except Exception as e:

           logging.error(f'Помилка в функції {func.__name__}: {e}')

           raise

   return wrapper

@logging_decorator

def simulate_gameplay(simulation_params):

 pass

