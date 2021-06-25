#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

void welcome() {
	string name;
	cout << "Your name: ";
	cin >> name;
	cout << "Hi, " + name + ".\n";
	cout << "Welcome to Jingze Dai's self introduction.\n";
	cout << "\n";
}

void introduction() {
	cout << "Hi, my name is Jingze Dai. \n";
	cout << "I am forth-year computer science coop student from McMaster University. \n";
	cout << "I have 2 years of Python, Java, C and C++ learning experience. \n";
	cout << "I learn a lot about Scala, Ruby and Haskell. \n";
	cout << "I am good at web programming (CSS, Javascript, Node.js, React.js and HTML). \n";
	cout << "I am interested with computer graphics so I learn OpenGL (glut library with C++) and Unity. \n";
	cout << "Other things: \n";
	cout << "Professional tools: Git, JSON, Unit Testing. \n";
	cout << "Assembly languages: MIPS32, NASM. \n";
	cout << "Database and Data Science: Oracle, MATLAB, SQL. \n";
	cout << "Linkedin Webpage: https://www.linkedin.com/in/jingze-dai/ \n";
	cout << "Github Webpage: https://github.com/daijingz \n";
}

void mygithub() {}

int main() {
	bool wantToReplay;
	string yesorno;
	string github;
	welcome();
	introduction();
	cout << "Do you want to see my github ? ";
	cin >> github;

	if ((github == "yes") || (github == "Yes")) {
		mygithub();
	}

	cout << "Do you want to see again? ";
	cin >> yesorno;

	if ((yesorno == "yes") || (yesorno == "Yes")) {
		wantToReplay = true;
	}
	else {
		wantToReplay = false;
	}

	if (wantToReplay == true) {
		main();
	}
	else {
		return 0;
	}
}