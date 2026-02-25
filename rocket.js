let i = 3
const interval = setInterval(() => {
    if(i>0){
        console.log(i)
        i--
    }else{
        console.log('Rocket flew......')
        clearInterval(interval)
    }
}, 1000)