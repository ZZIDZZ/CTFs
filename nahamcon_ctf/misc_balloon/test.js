var i
var j
var k
var l
var m
var n
var strs = "}{ abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&\\'()+,-./:;<=>?@[\\]^_`|~"

for (i=0;i<strs.length;i++){
    for(j=0;j<strs.length;j++){
        for(k=0;k<strs.length;k++){
            for (l=0;l<strs.length;l++){
                for(m=0;m<strs.length;m++){
                    for(n=0;n<strs.length;n++){
                        duar = strs[i]+strs[j]+ strs[k]+strs[l]+strs[m]+ strs[n]
                        if(duar !== (duar)){
                            console.log(strs[i],strs[j],strs[k],strs[l],strs[m],strs[n], duar !== (duar));
                        }
                    }
                }
            }
        }
    }
}