// Console.WriteLine("Введите пятизначное число число");
// int num = Convert.ToInt32(Console.ReadLine());
// string result = Convert.ToString(num);

// if (num >= 10000 && num < 100000)
// {
//     if (result[0]==result[4] && result[1]==result[3])
//     {
//         Console.WriteLine("Является  полиндромом");
//     }
//     else
//     {
//         Console.WriteLine("Не является полиндромом");
//     }
// }
// else
// {
//     Console.WriteLine("Число не входит  в этот промежуток");
// }



// Console.WriteLine("Введите число");
// int num = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Сумма = " + GetSum(num));

// int GetSum(int number)
// {
//     int sum = 0;
//     int count = 0;
//     while (number > count)
//     {


//         count++;
//         sum += count;
//     }
//     return sum;


// }





// Напишите программу, которая принимает на вход число и выдаёт количество цифр в числе.
// 456 -> 3
// 78 -> 2
// 89126 -> 5


// Console.WriteLine("Введите число");
// int num = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Количество цифр в числе:" + CountNumbers(num));

// int CountNumbers(string number) {
// // string count = number.Length;
// while(number>0){
//     int number = number % 10;
//     count++;
// }
// return count;
// }


// Console.WriteLine("Введите число:");
// int num = Convert.ToInt32(Console.ReadLine());
// string result = Convert.ToString(num);










// Console.WriteLine("Введите число:");
// int num = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Количество цифр в числе: " + GetCount(num));


// int GetCount(int number)
// {
//     int count = 0;
//     while (number > 0)
//     {
//         count++;
//         number /= 10;
//     }
//     return count;
// }





// Console.WriteLine("Введите число ");
//  int num = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Колличество цифр "+GetCount(num) );

//  int GetCount(int number)
//  {
//     int count =0;
//     while(number>0)
//     {
//         count++;
//         number/=10;

//     }
//     return count;

//  }




// string num = Console.ReadLine();
// int CountingDigits(string num)
// {
//     return num.Length;
// }
// Console.WriteLine(CountingDigits(num));




// Напишите программу, которая принимает на вход число N и выдаёт произведение чисел от 1 до N.
// 4 -> 24 
// 5 -> 120

// Console.WriteLine("Введите число ");
// int num = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Произведение = " + GetMult(num));

// int GetMult(int number)
// {
//     int mult = 1;
//     int count = 1;
//     while (number > count)
//     {
//         count++;
//         mult *= count;

//     }
//     return mult;
// }



// Напишите программу, которая выводит массив из 8 элементов, заполненный нулями и единицами в случайном порядке.
// [1,0,1,1,0,1,0,0]
int[] array = new int[8];

// заполняем массив
void FillArray(int[] collection) {
	int length = collection.Length;
	int index = 0;
	while (index < length) {
		collection[index] = new Random().Next(0, 2);
		index++;
	}
}

// выводим массив
void PrintArray(int[] col) {
	int count = col.Length;
	int position = 0;
	while (position < count) {
		Console.Write(col[position]);
		position++;
	}
}

FillArray(array);
PrintArray(array);







