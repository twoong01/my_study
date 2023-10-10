function calParkingFee(fee, parkingCar) {
    const [def_h, def_f, min, money] = fee;
    const result = Object.entries(parkingCar).map((car) => {
        const [num, time] = car;
        let totalFee;
        if(def_h >= time){
            totalFee = def_f;
        } else {
            totalFee = def_f + Math.ceil((time - def_h) / min) * money;
        }
        return {num, totalFee}
    })
    return result.sort((a, b) => a.num > b.num ? 1 : -1).map(({totalFee}) => Number(totalFee))
}

function solution(fees, records) {
    const parking = {};
    const parkingFee = {};
    const recordData = records.map((rec) => {
        const [time, num, state] = rec.split(' ');
        const [hour, min] = time.split(':').map((v) => Number(v));
        const minT = hour * 60 + min;
        if(state === 'IN'){
            parking[num] = minT;
        } else {
            const inTime = parking[num];
            if(parkingFee[num] === undefined){
                parkingFee[num] = (minT - inTime);
            } else {
                parkingFee[num] += (minT - inTime);
            }
            delete parking[num];
        }
    })
    
    Object.entries(parking).forEach((v) => {
        const [num, time] = v;
        const lastTime = 23 * 60 + 59;
        if(parkingFee[num] === undefined){
            parkingFee[num] = lastTime - time;
        } else {
            parkingFee[num] += lastTime - time;
        }
    })
    const result = calParkingFee(fees, parkingFee);
    return result;
}