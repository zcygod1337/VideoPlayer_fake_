#include<bits/stdc++.h>
#include<windows.h>
using namespace std;
void clearConsole() {
#if defined(_WIN32)
    system("cls");
#else
    system("clear");
#endif
}

const string FRAMES_FOLDER = "video";
string readAsciiFrame(int frame_number) {
    stringstream ss;
    ss << FRAMES_FOLDER << "/" << frame_number << ".txt";
    string file_path = ss.str();

    ifstream file(file_path);
    string frame_content;

    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            frame_content += line + "\n";
        }
        file.close();
    }

    return frame_content;
}
int fpsnow=1;
int main(){
	system("mode con cols=125 lines=35");
	cout << "¼´½«²¥·Å Bad apple, c++ player 1.0.0" << endl;
	Sleep(3000);
	system("cls"); 
	while(1){
		string ascii_frame = readAsciiFrame(fpsnow);
        if (ascii_frame.empty()) {
            break;
        }
//        system("cls");
		clearConsole();
        cout << ascii_frame;
        fpsnow++;
//		system("cls");
		Sleep(15);
	}
	return 0;
}
