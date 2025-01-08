# ID Generation and Replacement Guide

## Steps to Run the Script
1. **Run the script:**
   ```bash
   python gen_new_id.py
   ```

2. **Example Output:**
   Upon execution, you will see the following output:
   ```plaintext
   Generated Machine ID: auth0|user_1a2b3c4d5e6f7g8h9i0jklmnopqrstuvwxyzaabbccdd (Valid: True)
   Generated MAC Machine ID: 1a2b3c4d5e6f7g8h9i0jklmnopqrstuvwxyzaabbccddffgg (Valid: True)
   Generated Device ID: f47ac10b-58cc-4372-a567-0e02b2c3d479 (Valid: True)
   Generated SQM ID: {f47ac10b-58cc-4372-a567-0e02b2c3d479} (Valid: True)
   ```

## Important Notes:

### Copy Instructions
- When copying the Machine ID, **omit the `auth0|user_` prefix**.
  For example, from `auth0|user_1a2b3c4d5e6f7g8h9i0jklmnopqrstuvwxyzaabbccdd`,
  copy only:
  ```plaintext
  1a2b3c4d5e6f7g8h9i0jklmnopqrstuvwxyzaabbccdd
  ```

### Locate and Edit the JSON File
1. Navigate to the following directory:
   ```plaintext
   %AppData%/Cursor/User/globalStorage
   ```
2. Open the file named `storage.json` in a text editor.

### Replace the Following Keys
Find and update the corresponding fields with the newly generated IDs:

- **`telemetry.macMachineId`**: Replace with the **MAC Machine ID**.
- **`telemetry.sqmId`**: Replace with the **SQM ID**.
- **`telemetry.machineId`**: Replace with the **Machine ID** (without the prefix `auth0|user_`).
- **`telemetry.devDeviceId`**: Replace with the **Device ID**.

### Example JSON After Modification
```json
{
    "telemetry.macMachineId": "1a2b3c4d5e6f7g8h9i0jklmnopqrstuvwxyzaabbccddffgg",
    "telemetry.sqmId": "{f47ac10b-58cc-4372-a567-0e02b2c3d479}",
    "telemetry.machineId": "1a2b3c4d5e6f7g8h9i0jklmnopqrstuvwxyzaabbccdd",
    "telemetry.devDeviceId": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
}
```

## Final Steps
1. Ensure you **close the Cursor application** before modifying the `storage.json` file.
2. After making the changes, **restart Cursor** for the updates to take effect.

Enjoy your updated telemetry configuration!
