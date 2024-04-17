# Хук-Дживс
Метод Хук-Дживса поиска минимума функции:

1.	Выбор начальной точки поиска x<sub>0</sub>  = {x<sub>1</sub><sup>0</sup>, … x<sub>n</sub><sup>0</sup>}и начальное приращение Δx0
   
2.	Исследующий поиск
   
    a.	Пробный шаг x<sub>1</sub><sup>0</sup> + Δx<sup>0</sup>, вычисляем значение функции в точке x’ = (x<sub>1</sub><sup>0</sup> + Δx<sup>0</sup>, …, x<sub>n</sub><sup>0</sup>). Если значение в данной точке больше, чем значение в x<sub>0</sub>, то делаем пробный шаг в противоположном направлении по этой же переменной x” = (x<sub>1</sub><sup>0</sup> - Δx<sup>0</sup>, …, x<sub>n</sub><sup>0</sup>). Если и в этой точке значение функции больше, чем в изначальной, то оставляем точку  x<sub>1</sub><sup>0</sup> без изменений. Иначе заменяем x<sup>0</sup> на x’ или x”, соответственно.
  
    b.	Из вновь полученной точки делаем шаги по оставшимся координатам, используя тот же алгоритм. В итоге получаем точку x<sub>01</sub>
  
3.	Поиск по образцу
   
    a.	Определяем направление x<sub>01</sub> - x<sub>0</sub>, в котором функция уменьшается. 
  
    b.	Проводим минимизацию функции в указанном направлении, решая задачу        min<sub>λ</sub> f(x<sub>0</sub> + λ(x<sub>01</sub> – x<sub>0</sub>))
  
    c.	Величина шага по каждой переменной пропорциональна величине шага на этапе исследующего поиска. Если удастся сделать удачный шаг в поиске «по образцу», то в результате находим новое приближение x<sub>1</sub> = x<sub>0</sub> + λ<sup>0</sup>*(x<sub>01</sub> – x<sub>0</sub>), где λ<sup>0</sup> = argmin<sub>λ</sub> f(x<sub>0</sub> + λ*(x<sub>01</sub> – x<sub>0</sub>))
