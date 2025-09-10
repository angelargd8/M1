function add(a: integer, b: integer): integer {
    return a + b;
}

let result: integer = add(2, 3);    // ✅ correcto
// let error1 = add(2);             // ❌ error: faltan argumentos
// let error2 = add(2, true);       // ❌ error: tipo boolean no coincide con integer


function multiply(a: integer, b: integer): integer {
    return a * b;                  // ✅ retorno coincide con integer
}

function wrongReturn(a: integer): integer {
    return true;                 // ❌ error: boolean no coincide con integer
}


function factorial(n: integer): integer {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);    // ✅ llamada recursiva
}




let fact5: integer = factorial(5);  // 120
function greet(): string {
    return "Hello";
}

// function greet(): string {
//     return "Hi";           // ❌ error: redeclaración de función
// }
