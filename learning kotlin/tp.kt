//kotlinc tp.kt -include-runtime -d tp.jar
import java.util.Scanner
import kotlin.collections.mutableListOf
fun main(){


    val fruits = listOf("banana", "avocado", "apple", "kiwifruit")


    for (i in fruits){
        print(fruits.indices)
    } 
    fruits
        .filter { it.startsWith("a") }
        .sortedBy { it }
        .map{it.toUpperCase()}
        .forEach{print(it)}
    }

