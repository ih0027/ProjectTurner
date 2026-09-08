# Project Turner

An automated physical page-turning device controlled by a Raspberry Pi. This project utilizes continuous-rotation servos controlled via `pigpio` to manage mechanical spooling and turning actions, configured to launch reliably on boot as a background Linux systemd service.

## Project Structure

*   **`main.py`** – The core application managing input events and coordinates the servo sequence timing.
*   **`MotorUtils.py`** – A hardware abstraction layer wrapper for calibration and speed control of Feetech FS90R servos.
*   **`pageTurner.sh`** – An absolute-pathed execution entry script invoked directly by systemd.
*   **`pageTurner.service`** – The systemd configuration file enabling automated execution as root on system startup.
*   **`install.sh`** – An automated deployment script that provisions directories, copies configurations, and sets up system components.

## Hardware Setup

This project uses the **Feetech FS90R** continuous-rotation servo. Connect the hardware to your Raspberry Pi GPIO pins as follows:

| Component | Signal Pin (GPIO) | Target Frequency (Stop Calibration) |
| :--- | :--- | :--- |
| **Turn Servo** | GPIO 2 | 1495 µs |
| **Spool Servo** | GPIO 3 | 1435 µs |

*Ensure your servos have a shared common ground (GND) with the Raspberry Pi and are independently powered via an external 5V power supply to prevent brownouts.*

## Installation & Deployment

Clone or place your scripts into a temporary deployment directory (e.g., `~/scripts/` and `~/python/`) and run the setup sequence.

1. **Make the installer script executable:**
   ```bash
   chmod +x install.sh
   ```

2. **Execute the installation routine:**
   ```bash
   sudo ./install.sh
   ```

The script will automatically handle the system environment setup:
* Installs python3 if not already installed
* Installs, enables, and initializes the `pigpiod` daemon.
* Provisions directory routes at `/home/pi/pageTurner/`.
* Integrates and registers the `pageTurner.service` with the OS service manager.

## Service Management

You can actively manage, monitor, or debug the physical service in the background using native systemd commands:

*   **Check operational status or track error logs:**
    ```bash
    sudo systemctl status pageTurner
    ```
*   **Manually stop the execution sequence:**
    ```bash
    sudo systemctl stop pageTurner
    ```
*   **Restart the device routines manually:**
    ```bash
    sudo systemctl restart pageTurner
    ```

## Sequence Details

The automation handles page mechanics sequentially using relative speed constants (`1.0` full forward, `-1.0` full reverse):

1. **Forward Sequence (`turnPageForward`):** Retracts turn mechanism ➔ Unspools page wire ➔ Returns turn mechanism ➔ Extends spool home.
2. **Reverse Sequence (`turnPageReverse`):** Retracts spool wire ➔ Retracts turn mechanism ➔ Resets spool ➔ Resets turn mechanism home.
