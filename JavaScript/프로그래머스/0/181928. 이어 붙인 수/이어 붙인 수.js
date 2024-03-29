function solution(num_list) {
    var answer1 = 0;
    var answer2 = 0;
    for(i of num_list) {
        if(i % 2 == 1)
            answer1 += i.toString()
        else
            answer2 += i.toString()
    }
    var answer = parseInt(answer1, 10) + parseInt(answer2, 10)
    return answer;
}