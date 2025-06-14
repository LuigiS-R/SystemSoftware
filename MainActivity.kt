package com.example.finalproject

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.finalproject.ui.theme.FinalProjectTheme
import android.widget.*

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_login)

        //lateinit var dbHelper: MyDatabaseHelper

        //Finding views
        val usernameEditText :EditText = findViewById(R.id.usernameEditText)
        val pwEditText :EditText = findViewById(R.id.passwordEditText)
        val loginBtn: Button = findViewById(R.id.loginButton)
        val signupBtn :TextView= findViewById(R.id.signupLink)

        //dbHelper = MyDatabaseHelper(this)

        //SignUp Button

        signupBtn.setOnClickListener{
            val intent = Intent(this, SignUpActivity::class.java)
            startActivity(intent)
        }

        //LogIn Button
        loginBtn.setOnClickListener{
            var usernameInput = usernameEditText.text.toString(); var pwInput = pwEditText.text.toString()

            if (usernameInput.isBlank() || pwInput.isBlank()){
                Toast.makeText(this, "Make sure to fill all the fields", Toast.LENGTH_SHORT).show()
            }

            val results = dbHelper.getUsers(usernameInput)
            if (results.moveToFirst()){
                val pw = results.getString(results.getColumnIndexOrThrow("password"))
                if (pw == pwInput){
                    //LOGIN
                    var intent = Intent(this, HomeActivity::class.java)
                    startActivity(intent)
                }
                else{
                    Toast.makeText(this, "Password is incorrect", Toast.LENGTH_SHORT).show()
                }

            }
            else{
                Toast.makeText(this, "Username is incorrect", Toast.LENGTH_SHORT).show()
            }

        }



    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    FinalProjectTheme {
        Greeting("Android")
    }
}