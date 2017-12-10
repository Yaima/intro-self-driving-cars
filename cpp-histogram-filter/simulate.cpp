/**
	simulate.cpp

	Purpose: implements a Simulation class which
	simulates a robot living in a 2D world. Relies 
	on localization code from localizer.py 

	This file is incomplete! Your job is to make 
	this code work. 
*/

#include "localizer.cpp"

class Simulation {
	
private:
	vector <char> get_colors() {
		vector <char> all_colors;
		char color;
		int i,j;
		for (i=0; i<height; i++) {
			for (j=0; j<width; j++) {
				color = grid[i][j];
				if(std::find(all_colors.begin(), all_colors.end(), color) != all_colors.end()) {
				    /* v contains x */
				} else {
					all_colors.push_back(color);
					cout << "adding color " << color << endl;
				    /* v does not contain x */
				}
			}
		}
		colors = all_colors;
		num_colors = colors.size();
		return colors;
	}

public: 
	vector < vector <char> > grid;
	vector < vector <float> > beliefs;

	float blur, p_hit, p_miss, incorrect_sense_prob;

	int height, width, num_colors;
	
	std::vector<int> true_pose;
	std::vector<int> prev_pose;

	vector <char> colors;
	Simulation(vector < vector<char> >, float, float, vector <int>);

};

/**
Constructor for the Simulation class.
*/
Simulation::Simulation(vector < vector <char> > map, 
	float blurring,
	float hit_prob, 
	std::vector<int> start_pos
	) 
{
	grid = map;
	blur = blurring;
	p_hit = hit_prob;
	p_miss = 1.0;
	beliefs = initialize_beliefs(map);
	incorrect_sense_prob = p_miss / (p_hit + p_miss);
	true_pose = start_pos;
	prev_pose = true_pose;
}
