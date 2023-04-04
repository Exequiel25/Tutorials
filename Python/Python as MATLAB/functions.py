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
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    if show:
        plt.show()
    
    return xlim, ylim

def get_info(sys, grade=1):
    info = ctrl.step_info(sys)

    # Info:
    tr = info['RiseTime']
    ts = info['SettlingTime']
    tau = ts / 3.9769
    info['tau'] = tau

    if grade == 1:
        info['tr'] = tr
    elif grade == 2:
        tr = tau
        info['tr'] = tr

    return info

def plot_step_response_with_info(sys, t=None, show=True, grade=1):
    xlim, ylim = plot_step_response(sys, t, show=False)

    y = ylim[1]
    x = xlim[1]

    # Info:
    info = get_info(sys, grade)
    tr = info['tr']
    ts = info['SettlingTime']
    tau = info['tau']
    steady_state = info['SteadyStateValue']
    tp = info['PeakTime']
    Mp = info['Peak']

    
    # tp y Mp
    plt.plot(tp, Mp, 'rx', label='(tp, Mp)')
    plt.axvline(x=tp, ymin=0, ymax=Mp/y, color='r', linestyle='--')
    plt.axhline(y=Mp, xmin=0, xmax=tp/x, color='r', linestyle='--')
    
    # Settling time
    plt.axvline(x=ts, color='b', linestyle='--', label='ts')

    if grade == 1:
        plt.title('Step Response: Grade 1')
        # Rise time
        plt.axvline(x=tr, color='g', linestyle='--', label='tr')
        # tau
        plt.axvline(x=tau, ymin=0, ymax=0.632*Mp/y, color='y', linestyle='--')
        plt.axhline(y=0.632*Mp, xmin=0, xmax=tau/(x*0.8), color='y', linestyle='--')
        plt.plot(tau, 0.632*Mp, 'yx', label='(tau, 63.2%)')
    elif grade == 2:
        plt.title('Step Response: Grade 2')
        # Steady state
        plt.axhline(y=steady_state, color='k', linestyle='--', label='Steady State')
        # td
        plt.axhline(y=0.5*Mp, color='y', linestyle='--', label='50%')

    plt.xlabel('Time [sec]')
    plt.ylabel('Amplitude')
    plt.legend()
    if show:
        plt.show()

    return info

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
    poles, zeros = ctrl.pzmap(sys, plot=False)
    plt.scatter(poles.real, poles.imag, marker='x', color='r', label='Poles')
    plt.scatter(zeros.real, zeros.imag, marker='o', color='b', label='Zeros')
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlabel('Real Axis')
    plt.ylabel('Imaginary Axis')
    plt.title('Pole-Zero Map')
    plt.legend()
    plt.grid()
    if show:
        plt.show()
        
    return poles, zeros

def plot_nyquist(sys, show=True):
    omega = np.logspace(-2, 2, 1000)
    mag, phase, omega = ctrl.nyquist_plot(sys, omega)
    plt.grid()
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    if show:
        plt.show()
    
    return mag, phase, omega

def plot_rlocus(sys, show=True):
    ctrl.rlocus(sys)
    if show:
        plt.show()
