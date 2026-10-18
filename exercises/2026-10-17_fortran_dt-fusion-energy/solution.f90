! D-T fusion energy: your first Fortran program (FT-1.1)
! Build:  gfortran -Wall -fcheck=all solution.f90 -o solution
! Run:    ./solution

program dt_energy
  use, intrinsic :: iso_fortran_env, only: dp => real64
  implicit none

  ! --- Physical constants (do not change) ---------------------------------
  real(dp), parameter :: m_D   = 2.014101778_dp      ! deuterium, u
  real(dp), parameter :: m_T   = 3.016049281_dp      ! tritium, u
  real(dp), parameter :: m_He  = 4.002603254_dp      ! helium-4, u
  real(dp), parameter :: m_n   = 1.008664916_dp      ! neutron, u
  real(dp), parameter :: u_MeV = 931.49410242_dp     ! 1 u in MeV/c^2
  real(dp), parameter :: u_kg  = 1.66053906660e-27_dp ! 1 u in kg
  real(dp), parameter :: MeV_J = 1.602176634e-13_dp   ! 1 MeV in J

  ! --- Task 2 and 3: declare your variables here --------------------------


  ! --- Executable statements ----------------------------------------------
  print *, 'D-T fusion energy'

  ! Task 2: mass defect dm (u) and Q (MeV)

  ! Task 3: reactions per kg and energy per kg (J/kg)

end program dt_energy

! Task 4 (a) With implicit none, the compiler says:
! Task 4 (b) Without implicit none:
