PROGRAM symmetry
    INTEGER :: n,equal
    INTEGER, DIMENSION(:,:), ALLOCATABLE :: mat1,mat2
    READ(*,*)n
    ALLOCATE(mat1(n,n))
    ALLOCATE(mat2(n,n))
    CALL randMatHandle(n)
    OPEN(UNIT=101, FILE="mat1.txt")
    OPEN(UNIT=102, FILE="outSymm.txt")
    WRITE(102,*)"Taking input M from file mat1.txt"
    DO i=1,n
        DO j=1,n
            READ(101,'(I5)',ADVANCE='no')mat1(i,j)
            mat2(i,j) = mat1(i,j)
        END DO
        READ(101,*)
    END DO
    CALL t_pose(mat2,n)
    CALL equality(mat1,mat2,n,equal)
    IF(equal==0)THEN
        WRITE(102,*)"The matrix is not symmetric"
    ELSE
        WRITE(102,*)"The matrix is symmetric"
    END IF
END PROGRAM

SUBROUTINE t_pose(mat,n)
    INTEGER, INTENT(IN) :: n
    INTEGER, DIMENSION(n,n) :: mat
    INTEGER, DIMENSION(2) :: pos1,pos2
    DO i=1,n
        DO j=i,n
            pos1(1) = i
            pos1(2) = j
            pos2(1) = j
            pos2(2) = i
            CALL swap(mat,pos1,pos2,n)
        END DO
    END DO
END SUBROUTINE

SUBROUTINE equality(matA,matB,n,isEqual)
    INTEGER, INTENT(IN) :: n
    INTEGER, DIMENSION(n,n) :: matA,matB
    INTEGER, INTENT(OUT) :: isEqual
    isEqual = 1
    DO i=1,n
        DO j=1,n
            IF(matA(i,j)/=matB(i,j))THEN
                isEqual = 0
                EXIT
            END IF
        END DO
    END DO
END SUBROUTINE

SUBROUTINE swap(mat,pos1,pos2,n)
    INTEGER, INTENT(IN) :: n
    INTEGER, DIMENSION(2) :: pos1,pos2
    INTEGER, DIMENSION(n,n) :: mat
    INTEGER :: temp
    temp = mat(pos1(1),pos1(2))
    mat(pos1(1),pos1(2)) = mat(pos2(1),pos2(2))
    mat(pos2(1),pos2(2)) = temp
END SUBROUTINE

SUBROUTINE randMatCreate(n)
    INTEGER, INTENT(IN) :: n
    INTEGER :: m,l
    INTEGER :: values(8)
    REAL :: r
    INTEGER, DIMENSION(:), ALLOCATABLE :: seed
    CALL random_seed(size=l)
    ALLOCATE(seed(l))
    CALL date_and_time(values=values)
    seed = values(7)*values(8) + values(3)*values(4)
    CALL random_seed(put=seed)
    !PRINT*,"Order :"
    !READ(*,*)n
    !WRITE(*,*)"Entries of first matrix"
    OPEN(UNIT=101, FILE="mat1.txt")
    DO i=1,n**2
        CALL random_number(r)
        WRITE(101,'(I5)',ADVANCE='NO')NINT(10*r)
        IF(mod(i,n)==0)THEN
            WRITE(101,*)
        END IF
        seed = NINT(seed*r)
        CALL random_seed(put=seed)
    END DO
    CLOSE(101)
    !WRITE(*,*)"Entries of second matrix"
    seed = m-1
    CALL random_seed(put=seed)
    OPEN(UNIT=102, FILE="mat2.txt")
    DO i=1,n**2
        CALL random_number(r)
        WRITE(102,'(I5)',ADVANCE='NO')NINT(10*r)
        IF(mod(i,n)==0)THEN
            WRITE(102,*)
        END IF
        seed = NINT(seed*(r))
        CALL random_seed(put=seed)
    END DO
    CLOSE(102)
END SUBROUTINE

SUBROUTINE randMatHandle(n)
    INTEGER, INTENT(IN) :: n
    INTEGER :: randOption=1
    !PRINT*,"Press 0 to use default values in files, any other integer to create random numbers"
    !READ(*,*)randOption
    IF(randOption/=0)THEN
        CALL randMatCreate(n)
    END IF
END SUBROUTINE
