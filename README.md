# Алгоритмические задачи

(спринт 11,12,13)

## Задача 1. Структура данных - Дек (1.py).
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

***Внимание: при реализации используйте кольцевой буфер.***

### Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000. Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

### Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

### Пример
**Ввод**<br>
7<br>
10<br>
push_front -855<br>
push_front 0<br>
pop_back<br>
pop_back<br>
push_back 844<br>
pop_back<br>
push_back 823<br>

**Вывод**<br>
-855<br>
0<br>
844<br>

## Задача 2. Эффективная быстрая сортировка (2.py).
Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров. Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования будет определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов. Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память, то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place").

***Как работает in-place quick sort***
Как и в случае обычной быстрой сортировки, которая использует дополнительную память, необходимо выбрать опорный элемент (англ. pivot), а затем переупорядочить массив. Сделаем так, чтобы сначала шли элементы, не превосходящие опорного, а затем —– большие опорного.

Затем сортировка вызывается рекурсивно для двух полученных частей. Именно на этапе разделения элементов на группы в обычном алгоритме используется дополнительная память. Теперь разберёмся, как реализовать этот шаг in-place.

Пусть мы как-то выбрали опорный элемент. Заведём два указателя left и right, которые изначально будут указывать на левый и правый концы отрезка соответственно. Затем будем двигать левый указатель вправо до тех пор, пока он указывает на элемент, меньший опорного. Аналогично двигаем правый указатель влево, пока он стоит на элементе, превосходящем опорный. В итоге окажется, что что левее от left все элементы точно принадлежат первой группе, а правее от right — второй. Элементы, на которых стоят указатели, нарушают порядок. Поменяем их местами (в большинстве языков программирования используется функция swap()) и продвинем указатели на следующие элементы. Будем повторять это действие до тех пор, пока left и right не столкнутся.
На рисунке представлен пример разделения при pivot=5. Указатель left — голубой, right — оранжевый.


<div id="header" align="center">
  <img src="https://64.media.tumblr.com/31b595272b7314b4d4383a92921a8d9a/677e4cd55d5fa8e4-1f/s400x600/efd4076dafbf427aee6fd4c09f53377cb3a7ccbd.jpg"/>
</div>

### Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:

уникальным логином (строкой из маленьких латинских букв длиной не более 20)
числом решённых задач Pi
штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 10^9.

### Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному в строке.

### Пример
**Ввод**<br>
5<br>
alla 0 0<br>
gena 0 0<br>
gosha 0 0<br>
rita 0 0<br>
timofey 0 0<br>

**Вывод**<br>
alla<br>
gena<br>
gosha<br>
rita<br>
timofey<br>
