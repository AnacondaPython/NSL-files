using UnityEngine;
using System.Collections;

public class PlayerInput : MonoBehaviour
{
    public Rigidbody2D body;
    public float jumpcooldown = 2; //cooldown b/w jumps with space bar ...Add const so it doesn't change.
    private float jumptimer; //delay on how often you can jump

    // Use this for initialization
    void Start()
    {
        body = GetComponent<Rigidbody2D>();

    }

    // Update is called once per frame
    void Update()
    {


    }
    void FixedUpdate() //FixedUpdate updates every so often by a fixed interval (EDIT->Project Settings-> TIME ->Right hand side)
    {
        //body.AddForce(new Vector2(1, 9.8f));
        //body.AddTorque(5f);
        //float playerDirection.GetAxis("Horizontal");
        float xAccel = Input.GetAxis("Horizontal");
        body.AddForce(new Vector2(xAccel * 10, 0F));

        float yAccel = Input.GetAxis("Vertical");  //Vertical is predefined keyboard inputs up down arrow
        body.AddForce(new Vector2(0F, yAccel * 11)); //set this to 11 (to overcome gravity 9.8)

        if (jumptimer > 0)
        {
            jumptimer = jumptimer - Time.deltaTime; //FixedUpdate has a defined value of DeltaTime = 0.02 per fixedupdate http://i.imgur.com/Fe5E463.png
        }
        else
        {

            if (Input.GetKeyDown(KeyCode.Space)) //only true exact time you click item
            {
                body.AddForce(new Vector2(0, 10), ForceMode2D.Impulse);
                jumptimer = jumpcooldown;
            }
        }
    }
}
