"""
2021.06.15 수요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기
Chapter3. 기초 수학 첫걸음

4. 경사하강법 (순한맛)

"""


"""
1. 미분이 뭔가요 ?
- 미분(differentiation)은 변수의 움직임에 따른 함수 값의 변화를 측정하기 위한 도구
  최적화에서 가장 많이 사용하는 기법
- 변화율의 극한(limit)으로 정의한다.

f'(x) = lim(h->0) f(x + h) - f(x) / h
  -> 주어진 점 x에서 h만큼 이동한 점의 함수값의 차이를 h로 나눔 == 기울기, 변화율
     변화율의 극한 == 미분

- 미분을 손으로 계산하려면 일일이 h->0 극한을 계산해야 한다.

ex) 
# 손으로 계산
f(x) = x^2 + 2x + 3
f'(x) = 2x + 3  
  
# 파이썬으로 -> sympy.diff 사용
import sympy as sym
from sympy.abc import x

sym.diff(sym.poly(x ** 2 + 2 * x + 3), x)
 -> poly(2 * x + 2, x, domain='ZZ') 출력됨


* 미분을 이해해보자.
- 함수 f의 주어진 점 (x, f(X))과 x에서 h만큼 이동한 점 (x + h, f(x + h)) 사이를 
  이은 선이 f(x+h) - f(x) / h 이다.
  이 때, h를 점점 0으로 수렴하도록 만들어주게 되면
  (x, f(x))에서의 접선의 기울기로 수렴하게 된다.
  
- 증가시키고 싶다면 미분값을 더하고 감소시키고 싶으면 미분값을 뺀다.

- 한 점에서의 접선의 기울기를 알면 어느 방향으로 점을 움직여야
  함수 값이 증가하는지, 감소하는지 알수 있다.
  
- 미분값이 양수일 때는 미분값을 더하면 함수의 값이 증가하고 빼면 감소한다.
  
- 미분값(기울기)가 음수일 때 미분값을 더하면 뺄셈이 되고, 빼면 덧셈이 된다.
  따라서 더하면 함수의 값이 증가하고 빼면 함수의 값이 감소한다.
  
- 미분값을 더하면 경사상승법(gradient ascent)라 하며
  함수의 극댓값의 위치를 구할 때 사용한다.
    ->  목적함수를 최대화할 때 사용한다.

- 미분값을 빼면 경사하강법(gradient descent)라 하며
  함수의 극소값의 위치를 구할 때 사용한다.
    ->  목적함수를 최소화할 때 사용한다.
    
- 경사상승 / 경사하강 방법은 극값에 도달하면 움직임을 멈춘다.
  극값에선 미분값이 0 이므로 
  더이상 업데이트 되지 않아 목적함수의 최적화가 자동으로 멈춘다.
  
- 미분을 계산하려면 함수의 모양이 매끄러워야(연속) 한다.


* 경사하강법 알고리즘
Input : gradient(미분을 계산하는 함수), init(시작점), 
        lr(학습률), eps(알고리즘 종료 조건)
Output : var

var = init
grad = gradient(var)

while (abs(grad) > eps) :      # 컴퓨터로 계산할 때, 미분이 정확히 0이 되는 것은
                                 불가능, 따라서 eps보다 작을 때 종료하는 조건 필요
    var = var - lr * grad      # x - lambda f'(x)를 계산하는 부분.
                                 lr은 학습률로써 미분을 통해 업데이트 하는 속도 조절
    grad = gradient(var)       # var을 업데이트하며 위치 이동
    

* 변수가 벡터라면 ?
- 벡터가 입력인 다변수 함수의 경우 편미분(partial differentiation)을 사용
- 편미분 : 주어진 변수의 개수만큼 미분, 다른 변수는 상수 취급

ex)
수식
f(x, y) = x^2 + 2xy + 3 + cos(x + 2y)
axf(x, y) = 2x + 2y - sin(x + 2y)

코드
import sympy as sym
from sympy.abc import x, y

sym.diff(sym.poly(x**2 + 2*x*y + 3) + sym.cos(x + 2*y), x)
 >>> 2*x + 2*y - sin(x + 2*y)

- 각 변수 별로 편미분을 계산한 그래디언트 벡터를 경사하강 / 상승법에 사용
   ▽f = (ax1f, ax2f, ... , axdf)
     ▽ 는 nabla 라고 한다.
     앞서 사용한 미분값인 f'(x) 대신 벡터 ▽f를 사용하여
     x = (x1, ..., xd)를 동시에 업데이트 할 수 있다.


*
sin(x) 미분 == cos(x)
cos(x) 미분 == -sin(x)
tan(x) 미분 == 1 / cos^2(x)


* 그래디언트 벡터가 뭐에요 ?
f(x, y) = x^2 + 2y^2           

-▽f = -(2x, 4y)   
   : (x, y, z)라는 3차원 공간 상에서 f(x, y)표면을 따라
      그래디언트 벡터에 -를 붙여주게 되면 f(x, y)의 극소점을 향하는
      화살표들의 움직임을 볼수 있다.
      어떤 점에서 시작하든지 간에 화살표만 따라가기만 하면
      f(x, y)의 최소점으로 갈 수 있다.
      
      
* 경사하강법 알고리즘
Input : gradient, init, lr, eps
Output : var

var = init
grad = gradient(var)

while (norm(grad) > eps) :    # 경사하강법 알고리즘은 그대로 적용되나
                                벡터는 절대값 대신 노름을 계산해서 종료조건 설정
    var = var - lr * grad       
    grad = gradient(var)       
    

"""




