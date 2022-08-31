// Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.

// 1, 2, 5, 7, 19, 6, 1, 33 -> [1, 2, 5, 7, 19, 6, 1, 33]


// Вариант 1. Вывод рамдомного массива!

// int size = 8;
// int[] array = new int[size];
// Random myRandom = new Random();
 
// Console.WriteLine("Вывод с помощью for");
// for (int i = 0; i < array.Length; i++)
// {
//     array[i] = myRandom.Next(0, 10000);
//     Console.Write("{0} ", array[i]);
// }
 
// Console.WriteLine("\n\nВывод с помощью foreach");
// foreach (var elem in array)
// {
//     Console.Write("{0} ", elem);
// }
    
// Вариант 2. Вывод массива с помощью клавиатуры

  int size = 8;
  int[] array = new int[size];
  Console.WriteLine ("Введите элементы массива:" );
  for (int i=0; i < size; i++)
  {
   Console.Write("arrey [{0}] = ", i);
   array[i] = Convert.ToInt32(Console.ReadLine());
  }
  Console.Write("Массив заполнен. Вывести на экран (y/n)? ");
  string b = Console.ReadLine();
  if (b == "y")
  {
    for (int i = 0; i < size; i++)
    {
    Console.Write(array[i] + ", ");
    }
    Console.ReadKey();
  }