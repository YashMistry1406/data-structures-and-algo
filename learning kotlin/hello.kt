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

    val sc=Scanner(System.`in`)/*creating a variable of the scanner classjsut like java 
                                */
    
                            
                             
    
    println("enter age")
    var age=sc.nextInt()
    print(age)
//
//    when(age){
//        in 10..50->println("legal age")
//        else ->
//            {
//                println("illegal age")
//            }
//
//    }
    var allowed:String=when(age)
    {
        
        in 10..50->"legal age"
        else ->
            {
                "illegal age"
            }
    
        
    }
    println(allowed)
//("    labelled for loop in kotlin where we can assign loop 
    


    
        
}
