import java.util.Scanner
fun main(args: Array<String>) {
    val array = intArrayOf(1, 2, 3, 4, 5)    
    for (element in array) {
        println(element)
    }
    
    var new:Int=10 
    var personobj=person()
    personobj.name="Yash"
    println(personobj.name)

    val sc=Scanner(System.`in`)
    println("enter age")
    var age=sc.nextInt()
    print(age)

    var r=1..10
    println(r)


    
        
}
//fun main() {
//
//infix fun Int.times(str: String) = str.repeat(this)        // 1
//println(2 times "Bye ")                                    // 2
//
//val pair = "Ferrari" to "Katrina"                          // 3
//println(pair)
//
//infix fun String.onto(other: String) = Pair(this, other)   // 4
//val myPair = "McLaren" onto "Lucas"
//println(myPair)
//
//val sophia = Person("Sophia")
//val claudia = Person("Claudia")
//sophia likes claudia                                       // 5
//}
//
//class Person(val name: String) {
//val likedPeople = mutableListOf<Person>()
//infix fun likes(other: Person) { likedPeople.add(other) }  // 6
//}
