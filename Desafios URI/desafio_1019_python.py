'''Leia um valor inteiro, que é o tempo de duração em segundos de
um determinado evento em uma fábrica, e informe-o expresso no formato
horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para
horas:minutos:segundos, conforme exemplo fornecido.''''

N = int(input())

H = N//3600
N = N - H*3600

M = N//60
N = N - M*60

print("%d:%d:%d" %(H, M, N) )
