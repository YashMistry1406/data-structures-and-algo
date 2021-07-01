import java.util.Scanner
import kotlin.collections.mutableListOf
fun main(){
    val sc=Scanner(System.`in`)

    val user=arrayOf(1,2,3,4,5)
    val user_set=mutableListOf(9,8,7,6,5,4)
    var len=user_set.size
    println("$len")
    for (i in 0..len-1)
    {

        println(user_set[i])
    }
    }

