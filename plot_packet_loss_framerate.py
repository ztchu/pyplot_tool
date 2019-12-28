import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import json


def ParseParameters(input_json_file):
    with open(input_json_file) as json_file:
        paras = json.load(json_file)
        return paras

def GetData(txt_file):
    packet_loss_rate = []
    framerate = []
    with open(txt_file) as file:
        data = file.readlines()
        for num in data:
            packet_loss_rate.append(float(num.split(',')[0]))
            framerate.append(float(num.split(',')[1]))

    return (packet_loss_rate, framerate)



if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('--input', type=str, default="", help = "Json file include input parameters.")
    argv = parse.parse_args()

    input_files = ParseParameters(argv.input)
    labels = input_files['label']
    print(labels)

    all_packet_loss_rate =[[]]
    all_framerate = [[]]
    for one_record in input_files['input_file']:
        (packet_loss_rate, framerate) = GetData(one_record)
        all_packet_loss_rate.append(packet_loss_rate)
        all_framerate.append(framerate)

    if len(all_packet_loss_rate) > 1:
        del all_packet_loss_rate[0]

    if len(all_framerate) > 1:
        del all_framerate[0]

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    x_names = range(1, 33)
    x_names = [str(x) for x in list(x_names)]
    x = range(len(x_names))


    for index, result in enumerate(all_packet_loss_rate):
        ax1.plot(x, result, label=labels[index])

    for index, result in enumerate(all_framerate):
        ax2.plot(x, result, label=labels[index])

    ax1.legend()
    ax2.legend()
    plt.show()