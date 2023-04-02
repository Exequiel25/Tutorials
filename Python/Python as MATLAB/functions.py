import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

def plot_step_response(sys, t=None, show=True):
    t, y = ctrl.step_response(sys, t)
    plt.plot(t, y)
    plt.xlabel('Time [sec]')
    plt.ylabel('Amplitude')
    plt.title('Step Response')
    plt.grid()
    if show:
        plt.show()

def plot_step_response_info(info, show=True):
    K = info['Peak']
    Tp = info['PeakTime']
    ts = info['SettlingTime']
    plt.plot(Tp, K, 'b*', label='(Tp, K)')
    plt.axvline(x=ts, color='r', linestyle='--', label='ts')
    plt.axhline(y=0.632*K, color='k', linestyle='--', label='63,2%')

    tau = ts/3.9769
    plt.axvline(x=tau, color='g', linestyle='--', label='$T$')
    
    plt.legend()
    if show:
        plt.show()

    return K, Tp, ts, tau

def plot_impulse_response(sys, t=None, show=True):
    t, y = ctrl.impulse_response(sys, t)
    plt.plot(t, y)
    plt.xlabel('Time [sec]')
    plt.ylabel('Amplitude')
    plt.title('Impulse Response')
    plt.grid()
    if show:
        plt.show()

def plot_bode(sys, show=True):
    w, mag, phase = ctrl.bode(sys)
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag)    # Bode magnitude plot
    plt.grid()
    plt.ylabel('Magnitude [dB]')
    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase)  # Bode phase plot
    plt.grid()
    plt.ylabel('Phase [deg]')
    plt.xlabel('Frequency [rad/sec]')
    if show:
        plt.show()

def plot_pzmap(sys, show=True):
    ctrl.pzmap(sys)
    if show:
        plt.show()

def plot_nyquist(sys, show=True):
    omega = np.logspace(-2, 2, 1000)
    mag, phase, omega = ctrl.nyquist_plot(sys, omega)
    plt.grid()
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    if show:
        plt.show()

def plot_rlocus(sys, show=True):
    ctrl.rlocus(sys)
    if show:
        plt.show()
