package com.example.mdp22;


import android.Manifest;
import android.app.AlertDialog;
import android.app.ProgressDialog;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;

import android.os.Handler;
import android.text.method.ScrollingMovementMethod;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import java.math.BigInteger;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Set;
import java.util.UUID;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class BluetoothFragment extends Fragment{
    private static final String TAG = "BluetoothConnect";

    // Declarations
    public ArrayList<BluetoothDevice> mNewBTDevices;
    public ArrayList<BluetoothDevice> mPairedBTDevices;
    public DeviceListAdapter mNewDevlceListAdapter;
    public DeviceListAdapter mPairedDevlceListAdapter;

    BluetoothAdapter mBluetoothAdapter;
    ListView lvNewDevices;
    ListView lvPairedDevices;
    Button btnSend;
    EditText sendMessage;
    Button btnSearch;
    StringBuilder incomingMsg;
    TextView incomingMsgTextView;
    Button connectBtn;
    TextView deviceSearchStatus;
    ProgressDialog myProgressDialog;
    TextView pairedDeviceText;
    SharedPreferences sharedPreferences;
    SharedPreferences.Editor editor;
    TextView connStatusTextView;
    String connStatus;
    ProgressDialog myDialog;

    com.example.mdp26.BluetoothConnectionService mBluetoothConnection;
    // UUID
    private static final UUID myUUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
    public static BluetoothDevice mBTDevice;

    boolean retryConnection = false;
    Handler reconnectionHandler = new Handler();

    Runnable reconnectionRunnable = new Runnable() {
        @Override
        public void run() {
            // Magic here
            try {
                if (com.example.mdp26.BluetoothConnectionService.BluetoothConnectionStatus == false) {
                    startBTConnection(mBTDevice, myUUID);
                    Toast.makeText(getContext(), "Reconnection Success", Toast.LENGTH_SHORT).show();

                }
                reconnectionHandler.removeCallbacks(reconnectionRunnable);
                retryConnection = false;
            } catch (Exception e) {
                Toast.makeText(getContext(), "Failed to reconnect, trying in 5 second", Toast.LENGTH_SHORT).show();
            }
        }
    };

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_bluetooth,container, false);
    }


    public void onViewCreated(View view, Bundle savedInstanceState) {

        connectBtn = getActivity().findViewById(R.id.connectBtn);
        btnSearch = getActivity().findViewById(R.id.searchBtn);
        lvNewDevices = getActivity().findViewById(R.id.listNewDevice);
        lvPairedDevices = getActivity().findViewById(R.id.pairedDeviceList);
        btnSend = getActivity().findViewById(R.id.btnSend);
        sendMessage = getActivity().findViewById(R.id.messageText);
        incomingMsgTextView = getActivity().findViewById(R.id.incomingText);
        deviceSearchStatus = getActivity().findViewById(R.id.deviceSearchStatus);
        pairedDeviceText = getActivity().findViewById(R.id.pairedDeviceText);
        incomingMsg = new StringBuilder();
        connStatusTextView = (TextView) getActivity().findViewById(R.id.connStatusTextView);

        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        mNewBTDevices = new ArrayList<>();
        mPairedBTDevices = new ArrayList<>();

        incomingMsgTextView.setMovementMethod(new ScrollingMovementMethod());

        getActivity().registerReceiver(myReceiver, new IntentFilter("incomingMessage"));

        IntentFilter filter = new IntentFilter(BluetoothDevice.ACTION_BOND_STATE_CHANGED);
        getActivity().registerReceiver(mBroadcastReceiver4, filter);

        IntentFilter filter2 = new IntentFilter("ConnectionStatus");
        getActivity().registerReceiver(mBroadcastReceiver5, filter2);

        lvNewDevices.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                mBluetoothAdapter.cancelDiscovery();
                lvPairedDevices.setAdapter(mPairedDevlceListAdapter);

                String deviceName = mNewBTDevices.get(i).getName();
                String deviceAddress = mNewBTDevices.get(i).getAddress();
                Log.d(TAG, "onItemClick: A device is selected.");
                Log.d(TAG, "onItemClick: DEVICE NAME: " + deviceName);
                Log.d(TAG, "onItemClick: DEVICE ADDRESS: " + deviceAddress);

                if (Build.VERSION.SDK_INT > Build.VERSION_CODES.JELLY_BEAN_MR2) {
                    Log.d(TAG, "onItemClick: Initiating pairing with " + deviceName);
                    mNewBTDevices.get(i).createBond();

                    mBluetoothConnection = new com.example.mdp26.BluetoothConnectionService(getActivity());
                    mBTDevice = mNewBTDevices.get(i);
                }
            }
        });

        lvPairedDevices.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                mBluetoothAdapter.cancelDiscovery();
                lvNewDevices.setAdapter(mNewDevlceListAdapter);

                String deviceName = mPairedBTDevices.get(i).getName();
                String deviceAddress = mPairedBTDevices.get(i).getAddress();
                Log.d(TAG, "onItemClick: A device is selected.");
                Log.d(TAG, "onItemClick: DEVICE NAME: " + deviceName);
                Log.d(TAG, "onItemClick: DEVICE ADDRESS: " + deviceAddress);

                mBluetoothConnection = new com.example.mdp26.BluetoothConnectionService(getActivity());
                mBTDevice = mPairedBTDevices.get(i);
            }
        });

        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //showLog("Clicked sendTextBtn");
                String sentText = "" + sendMessage.getText().toString();

                SharedPreferences.Editor editor = sharedPreferences.edit();
                editor.putString("message", sharedPreferences.getString("message", "") + '\n' + sentText);
                editor.commit();
                //messageReceivedTextView.setText(sharedPreferences.getString("message", ""));
                sendMessage.setText("");

                if (com.example.mdp26.BluetoothConnectionService.BluetoothConnectionStatus == true) {
                    byte[] bytes = sentText.getBytes(Charset.defaultCharset());
                    com.example.mdp26.BluetoothConnectionService.write(bytes);
                }
            }
        });


        connectBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(mBTDevice ==null)
                {
                    Toast.makeText(getContext(), "Please Select a Device before connecting.", Toast.LENGTH_LONG).show();
                }
                else {
                    startConnection();
                }
            }
        });

        connStatusTextView = getActivity().findViewById(R.id.connStatusTextView);
        connStatus ="Disconnected";
        sharedPreferences = getContext().getSharedPreferences("Shared Preferences", Context.MODE_PRIVATE);
        if (sharedPreferences.contains("connStatus"))
            connStatus = sharedPreferences.getString("connStatus", "");

        connStatusTextView.setText(connStatus);

        myDialog = new ProgressDialog(getContext());
        myDialog.setMessage("Waiting for other device to reconnect...");
        myDialog.setCancelable(false);
        myDialog.setButton(DialogInterface.BUTTON_NEGATIVE, "Cancel", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.dismiss();
            }
        });

        btnSearch.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                toggleButtonScan(view);
            }
        });
    }

    public void toggleButtonScan(View view){
        Log.d(TAG, "toggleButton: Scanning for unpaired devices.");
        mNewBTDevices.clear();
        if(mBluetoothAdapter != null) {
            if (!mBluetoothAdapter.isEnabled()) {
                Toast.makeText(getContext(), "Please turn on Bluetooth first!", Toast.LENGTH_SHORT).show();
            }
            if (mBluetoothAdapter.isDiscovering()) {
                mBluetoothAdapter.cancelDiscovery();
                Log.d(TAG, "toggleButton: Cancelling Discovery.");

                checkBTPermissions();

                mBluetoothAdapter.startDiscovery();
                IntentFilter discoverDevicesIntent = new IntentFilter(BluetoothDevice.ACTION_FOUND);
                getActivity().registerReceiver(mBroadcastReceiver3, discoverDevicesIntent);
            } else if (!mBluetoothAdapter.isDiscovering()) {
                checkBTPermissions();

                mBluetoothAdapter.startDiscovery();
                IntentFilter discoverDevicesIntent = new IntentFilter(BluetoothDevice.ACTION_FOUND);
                getActivity().registerReceiver(mBroadcastReceiver3, discoverDevicesIntent);
            }
            mPairedBTDevices.clear();
            Set<BluetoothDevice> pairedDevices = mBluetoothAdapter.getBondedDevices();
            Log.d(TAG, "toggleButton: Number of paired devices found: "+ pairedDevices.size());
            for(BluetoothDevice d : pairedDevices){
                Log.d(TAG, "Paired Devices: "+ d.getName() +" : " + d.getAddress());
                mPairedBTDevices.add(d);
                mPairedDevlceListAdapter = new DeviceListAdapter(getContext(), R.layout.device_adapter_view, mPairedBTDevices);
                lvPairedDevices.setAdapter(mPairedDevlceListAdapter);
            }
        }
    }



    private void checkBTPermissions() {
        if(Build.VERSION.SDK_INT > Build.VERSION_CODES.LOLLIPOP){
            int permissionCheck = getContext().checkSelfPermission("Manifest.permission.ACCESS_FINE_LOCATION");
            permissionCheck += getContext().checkSelfPermission("Manifest.permission.ACCESS_COARSE_LOCATION");
            if (permissionCheck != 0) {
                this.requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION}, 1001);
            }
        } else {
            Log.d(TAG, "checkBTPermissions: No need to check permissions. SDK version < LOLLIPOP.");

        }
    }
    private final BroadcastReceiver mBroadcastReceiver1 = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(mBluetoothAdapter.ACTION_STATE_CHANGED)) {
                final int state = intent.getIntExtra(BluetoothAdapter.EXTRA_STATE, BluetoothAdapter.ERROR);

                switch (state) {
                    case BluetoothAdapter.STATE_OFF:
                        Log.d(TAG, "mBroadcastReceiver1: STATE OFF");
                        break;
                    case BluetoothAdapter.STATE_TURNING_OFF:
                        Log.d(TAG, "mBroadcastReceiver1: STATE TURNING OFF");
                        break;
                    case BluetoothAdapter.STATE_ON:
                        Log.d(TAG, "mBroadcastReceiver1: STATE ON");

                        break;
                    case BluetoothAdapter.STATE_TURNING_ON:
                        Log.d(TAG, "mBroadcastReceiver1: STATE TURNING ON");
                        break;
                }
            }
        }
    };
    private final BroadcastReceiver mBroadcastReceiver2 = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals(mBluetoothAdapter.ACTION_SCAN_MODE_CHANGED)) {
                final int mode = intent.getIntExtra(BluetoothAdapter.EXTRA_SCAN_MODE, BluetoothAdapter.ERROR);

                switch (mode) {
                    case BluetoothAdapter.SCAN_MODE_CONNECTABLE_DISCOVERABLE:
                        Log.d(TAG, "mBroadcastReceiver2: Discoverability Enabled.");
                        break;
                    case BluetoothAdapter.SCAN_MODE_CONNECTABLE:
                        Log.d(TAG, "mBroadcastReceiver2: Discoverability Disabled. Able to receive connections.");
                        break;
                    case BluetoothAdapter.SCAN_MODE_NONE:
                        Log.d(TAG, "mBroadcastReceiver2: Discoverability Disabled. Not able to receive connections.");
                        break;
                    case BluetoothAdapter.STATE_CONNECTING:
                        Log.d(TAG, "mBroadcastReceiver2: Connecting...");
                        break;
                    case BluetoothAdapter.STATE_CONNECTED:
                        Log.d(TAG, "mBroadcastReceiver2: Connected.");
                        break;
                }
            }
        }
    };
    public BroadcastReceiver mBroadcastReceiver3 = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            Log.d(TAG, "onReceive: ACTION FOUND.");

            if(action.equals(BluetoothDevice.ACTION_FOUND)) {
                BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                mNewBTDevices.add(device);
                Log.d(TAG, "onReceive: "+ device.getName() +" : " + device.getAddress());
                mNewDevlceListAdapter = new DeviceListAdapter(context, R.layout.device_adapter_view, mNewBTDevices);
                lvNewDevices.setAdapter(mNewDevlceListAdapter);

            }
        }
    };
    private BroadcastReceiver mBroadcastReceiver4 = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();

            if(action.equals(BluetoothDevice.ACTION_BOND_STATE_CHANGED)){
                BluetoothDevice mDevice = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                if(mDevice.getBondState() == BluetoothDevice.BOND_BONDED){
                    Log.d(TAG, "BOND_BONDED.");
                    Toast.makeText(getContext(), "Successfully paired with " + mDevice.getName(), Toast.LENGTH_SHORT).show();
                    mBTDevice = mDevice;
                }
                if(mDevice.getBondState() == BluetoothDevice.BOND_BONDING){
                    Log.d(TAG, "BOND_BONDING.");
                }
                if(mDevice.getBondState() == BluetoothDevice.BOND_NONE){
                    Log.d(TAG, "BOND_NONE.");
                }
            }
        }
    };

    BroadcastReceiver messageReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            String message = intent.getStringExtra("receivedMessage");
            incomingMsgTextView.setText(message +"\n");
        }
    };

    public BroadcastReceiver mBroadcastReceiver5 = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            BluetoothDevice mDevice = intent.getParcelableExtra("Device");
            String status = intent.getStringExtra("Status");
            sharedPreferences = getContext().getSharedPreferences("Shared Preferences", Context.MODE_PRIVATE);
            editor = sharedPreferences.edit();

            if(status.equals("connected")){
                try {
                    myDialog.dismiss();
                } catch(NullPointerException e){
                    e.printStackTrace();
                }

                Log.d(TAG, "mBroadcastReceiver5: Device now connected to "+mDevice.getName());
                Toast.makeText(getContext(), "Device now connected to "+mDevice.getName(), Toast.LENGTH_LONG).show();
                editor.putString("connStatus", "Connected to " + mDevice.getName());
                connStatusTextView.setText("Connected to " + mDevice.getName());

            }
            else if(status.equals("disconnected") && retryConnection == false){
                Log.d(TAG, "mBroadcastReceiver5: Disconnected from "+mDevice.getName());
                Toast.makeText(getContext(), "Disconnected from "+mDevice.getName(), Toast.LENGTH_LONG).show();
                mBluetoothConnection = new com.example.mdp26.BluetoothConnectionService(getActivity());
//                mBluetoothConnection.startAcceptThread();


                sharedPreferences = getContext().getSharedPreferences("Shared Preferences", Context.MODE_PRIVATE);
                editor = sharedPreferences.edit();
                editor.putString("connStatus", "Disconnected");
                TextView connStatusTextView = getActivity().findViewById(R.id.connStatusTextView);
                connStatusTextView.setText("Disconnected");
                editor.commit();

                try {
                    myDialog.show();
                }catch (Exception e){
                    Log.d(TAG, "BluetoothPopUp: mBroadcastReceiver5 Dialog show failure");
                }
                retryConnection = true;
                reconnectionHandler.postDelayed(reconnectionRunnable, 15000);

            }
            editor.commit();
        }
    };

    public void startConnection(){
        startBTConnection(mBTDevice,myUUID);

    }

    BroadcastReceiver myReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {

            Log.d(TAG, "Receiving Message!");

            String msg = intent.getStringExtra("receivedMessage");
            incomingMsg.append(msg + "\n");
            incomingMsgTextView.setText(incomingMsg);

        }
    };

    public void startBTConnection(BluetoothDevice device, UUID uuid){
        Log.d(TAG, "startBTConnection: Initializing RFCOM Bluetooth Connection");

        mBluetoothConnection.startClientThread(device, uuid);
    }

    @Override
    public void onDestroy() {
        Log.d(TAG, "onDestroy: called");
        super.onDestroy();
        try {
            getActivity().unregisterReceiver(mBroadcastReceiver1);
            getActivity().unregisterReceiver(mBroadcastReceiver2);
            getActivity().unregisterReceiver(mBroadcastReceiver3);
            getActivity().unregisterReceiver(mBroadcastReceiver4);
            getActivity().unregisterReceiver(mBroadcastReceiver5);
            getActivity().unregisterReceiver(myReceiver);
        } catch(IllegalArgumentException e){
            e.printStackTrace();
        }
    }

    @Override
    public void onPause() {
        Log.d(TAG, "onPause: called");
        super.onPause();
        try {
            getActivity().unregisterReceiver(mBroadcastReceiver1);
            getActivity().unregisterReceiver(mBroadcastReceiver2);
            getActivity().unregisterReceiver(mBroadcastReceiver3);
            getActivity().unregisterReceiver(mBroadcastReceiver4);
            getActivity().unregisterReceiver(mBroadcastReceiver5);
        } catch(IllegalArgumentException e){
            e.printStackTrace();
        }
    }

//    @Override
//    public void finish() {
//        Intent data = new Intent();
//        data.putExtra("mBTDevice", mBTDevice);
//        data.putExtra("myUUID",myUUID);
//        setResult(RESULT_OK, data);
//        super.finish();
//    }
}





