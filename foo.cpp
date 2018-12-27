
#include <iostream>
// A simple class with a constuctor and some methods...
class Foo
{
    public:
        Foo(int);
        void bar();
        int foobar(int);
        char* show(std::string str);
    private:
        int val;
};

Foo::Foo(int n)
{
    val = n;
}

void Foo::bar()
{
    std::cout << "Value is " << val << std::endl;
}

int Foo::foobar(int n)
{
    return val + n;
}

char* Foo::show(std::string str)
{
  str+="; lemao";
  return &str[0];
}

extern "C"
{
    Foo* Foo_new(int n) {return new Foo(n);}
    void Foo_bar(Foo* foo) {foo->bar();}
    int Foo_foobar(Foo* foo, int n) {return foo->foobar(n);}
    char* Foo_show(Foo* foo, char* str) {return foo->show(str);}
}



