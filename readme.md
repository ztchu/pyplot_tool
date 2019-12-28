A simple script to draw curves according to input file.

The input file is in json format, just like this:
```
{
    "input_file":[
        "5_G_test/no_loss_record_stats.txt",
        "5_G_test/20_loss_record_stats.txt",
        "5_G_test/40_loss_record_stats.txt"
    ],
    "label":[
        "no_loss",
        "20_percent_loss",
        "40_percent_loss"
    ]
}
```

It can be used in this way on windows platform:    
`py -3 plot_packet_loss_framerate.py --input input.json`