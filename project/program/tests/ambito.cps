let globalVar: integer = 10; // variable global

function testScope() {
    let localVar: integer = 5; // variable local
    print(globalVar);          // se puede acceder a variable global
    print(localVar);           // se puede acceder a variable local
}

function useUndeclared() {
    // print(x);             // ❌ error: x no está declarada
    let x: integer = 20;    // ahora sí está declarada
    print(x);               //  correcto
}


let a: integer = 5;
// let a: integer = 10;    // ❌ error: redeclaración en el mismo ámbito

function f() {
    let a: integer = 2;     //  permitido: nuevo ámbito local
    print(a);
}

function nestedBlocks() {
    let x: integer = 1;
    {
        let y: integer = 2;
        print(x);           //  se puede acceder a variable del bloque externo
        print(y);           //  se puede acceder a variable del bloque actual
    }
    // print(y);             // ❌ error: y solo existe en el bloque interno
}


let g: integer = 100; // entorno global

function outer() {
    let x: integer = 10; // entorno de la función outer
    
    function inner() {
        let x: integer = 5;  // entorno de la función inner
        let y: integer = 20; // también en el entorno de inner
        print(x);             // 5
        print(y);             // 20
        print(g);             // 100, acceso a entorno global
    }
    
    inner();
    // print(y);             // ❌ error: y no existe en outer
    print(x);               // 10
}

outer();
