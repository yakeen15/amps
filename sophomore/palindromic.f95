Program palindrome 
    Implicit none
    integer::n,rev=0,m,k
    Print*,"Enter a number: "
    read*,n
    k=n
    do while(n/=0)
        m=mod(n,10)
        rev=rev*10+m
        n=n/10
    end do
    if(k==rev)then
        print*,"Palindrome number"
    else
        print*,"Not palindrome"
    end if
end program palindrome