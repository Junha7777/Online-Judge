function solution(num_list) {
    let k = 0;
    let j = 1;
    let a = 0;
    for(i of num_list) {
        k = k + i
        j = j * i
    }
    k = k**2
    if(k > j)
        a = 1
    else
        a = 0
    return a;
}