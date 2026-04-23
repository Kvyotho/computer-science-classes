package com.mycompany.notes;

/* class notes >>
write in paper instead of java comments next time or later
relationships and association
>high cohesion and low acoplamento

-unidirecional or bidirectional
>>uni = a uses b, b doesnt uses a
>>bi = a uses b, b uses a

-agregacao
>todo-parte
>car and wheels example
>>they can exist without eachother
high cohesion -> makes no sense to have a car without wheels (but you can for whatever reason)

-associar =/= agregar
just looking at a snippet of the source code, you cannot define which one it is,
you need to look at context
trickster question

-composicao
>some relationships are dependant on something else existing
pedido (closed diamond)<-- itens
so itens only exist if pedido exists

-open diamond = agregacao(/associacao?)
-closed diamond = composicao

>no diamonds on test/source code,
review the code to say which one it is
>refer to slides to proper instructions and images
as to composicao x agregacao x associacao
 */



public class Notes {

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
