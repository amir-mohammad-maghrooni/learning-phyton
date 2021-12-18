using System;

namespace maghrooni_product
{
    class product
    {
        
        private int toy_number1=23;
        private double toy_number2=12.53;
        private int toy_number3=40;
        private double toy_number4=15.99;
        
        public int _toy_number1
        {
            get
            {
                return toy_number1;
            }
        }
        public double _toy_number2
        {
            get
            {
                return toy_number2;
            }
        }
        public int _toy_number3
        {
            get
            {
                return toy_number3;
            }
        }
        public double _toy_number4
        {
            get
            {
                return toy_number4;
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            string name;
            product obj_p = new product();
            string answ = "no"; string answ2 = "no";
            bool cont = false; bool cont2 = false;
            int product_list;
            double pro_price=0;
            string address = "NA";

            Console.WriteLine(DateTime.Now);

            Console.WriteLine("hello and welcome to the toy store;\nplease enter your first name");
            name = Console.ReadLine();
            do
            {

                Console.WriteLine("welcome back mr/mrs " + name);

                Console.WriteLine("there are 4 items on your wishlist,\nbecaus of the limited stock you can order on of each item;\nthe first items price is:" + obj_p._toy_number1 + "$\nthe second items price is:" + obj_p._toy_number2 + "$");
                Console.WriteLine("the third items price is:" + obj_p._toy_number3 + "$\nthe forth items price is:" + obj_p._toy_number4 + "$");

                Console.WriteLine("witch items would you like to by?\n(1,2,3,4,5=al,6=123,7=234,8=134,9=124, 12,21=1&2 13,31=1&3 14,41=1&4 23,31=2&3 24,42=2&4 34,43=3&4)"); 
                product_list =int.Parse(Console.ReadLine());
                switch (product_list)
                {
                    case 1:
                        pro_price = 23;
                        break;
                    case 2:
                        pro_price = 12.53;
                        break;
                    case 3:
                        pro_price = 40;
                        break;
                    case 4:
                        pro_price = 15.99;
                        break;
                    case 5:
                        pro_price = (23 + 12.53) + (40 + 15.99);
                        break;
                    case 6:
                        pro_price = (23 + 12.53) + 40;
                        break;
                    case 7:
                        pro_price = (12.53 + 40) + 15.99;
                        break;
                    case 8:
                        pro_price = (23 + 40) + 15.99;
                        break;
                    case 9:
                        pro_price = (23 + 12.53) + 15.99;
                        break;
                    case 12:
                        pro_price = 23 + 12.53;
                        break;
                    case 13:
                        pro_price = 23 + 40;
                        break;
                    case 14:
                        pro_price = 23 + 15.99;
                        break;
                    case 21:
                        pro_price = 23 + 12.53;
                        break;
                    case 23:
                        pro_price = 12.53 + 40;
                        break;
                    case 24:
                        pro_price = 12.53 + 15.99;
                        break;
                    case 31:
                        pro_price = 40 + 23;
                        break;
                    case 32:
                        pro_price = 40 + 12.53;
                        break;
                    case 34:
                        pro_price = 40 + 15.99;
                        break;
                    case 41:
                        pro_price = 15.99 + 23;
                        break;
                    case 42:
                        pro_price = 15.99 + 12.53;
                        break;
                    case 43:
                        pro_price = 15.99 + 40;
                        break;
                    default:
                        pro_price = 0;
                        break;
                }

                Console.WriteLine("your name is:" + name + "\ntotal product price =" + pro_price);

                Console.WriteLine("are these correct? yes.no");
                answ = Console.ReadLine();
                if (answ != "no" && answ != "No" && answ != "NO" && answ != "nO")
                    cont = true;
            }
            while (cont == false);
            do
            {
                Console.WriteLine("while we prosses your order will you kindly enter your address?");
                address = Console.ReadLine();
                Console.WriteLine("your address is:\n" + address);
                Console.WriteLine("is this correct? yes.no");
                answ2 = Console.ReadLine();
                if (answ2 != "no" && answ2 != "No" && answ2 != "NO" && answ2 != "nO")
                    cont2 = true;
            }
            while (cont2 == false);

            Console.WriteLine("we will ship the toys valued:" + pro_price + "\nto the address:" + address);
            Console.WriteLine("to the mr/mrs " + name);
            Console.WriteLine("we thank you for your order!\nthe order will reach you in the following week");

            Console.ReadKey();
        }
    }
}
