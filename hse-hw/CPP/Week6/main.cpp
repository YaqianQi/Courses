
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

enum class Day { Mon, Tue, Wed, Thu, Fri, Sat, Sun };

class Record {
private:
    std::string employeeName;
    int age;
    std::string department;
    std::string position;
    std::string bossName;
    std::set<Day> workingDays;

 public:
    // Constructor that takes individual attributes
    Record(){};
    Record(std::string& name, int employeeAge, std::string& employeeDepartment,
           std::string& employeePosition, std::string& boss, std::set<Day>& days)
        : employeeName(name), age(employeeAge), department(employeeDepartment),
          position(employeePosition), bossName(boss), workingDays(days) {}
    Record(const std::string& line, char delimiter = ',') {
            std::stringstream ss(line);
            std::string token;

            // Extracting attributes from the line
            std::getline(ss, token, delimiter);
            employeeName = token;

            std::getline(ss, token, delimiter);
            age = std::stoi(token);

            std::getline(ss, token, delimiter);
            department = token;

            std::getline(ss, token, delimiter);
            position = token;

            std::getline(ss, token, delimiter);
            bossName = token;

            while (std::getline(ss, token, delimiter)) {
                if (token == "Mon")
                    workingDays.insert(Day::Mon);
                else if (token == "Tue")
                    workingDays.insert(Day::Tue);
                else if (token == "Wed")
                    workingDays.insert(Day::Wed);
                else if (token == "Thu")
                    workingDays.insert(Day::Thu);
                else if (token == "Fri")
                    workingDays.insert(Day::Fri);
                else if (token == "Sat")
                    workingDays.insert(Day::Sat);
                else if (token == "Sun")
                    workingDays.insert(Day::Sun);
            }
        }

    friend std::ostream& operator<<(std::ostream& os, const Record& record) {
        os << "Employee Name: " << record.employeeName << ", ";
        os << "Department: " << record.department << ", ";
        os << "Position: " << record.position << ", ";
        os << "Boss Name: " << (record.bossName.empty() ? "N/A" : record.bossName);
        return os;
    }

    const std::string& getEmployeeName() const{
        return employeeName;
    }
    const std::string& getDepartment() const{
        return department;
    }

    const std::string& getBossName() const{
        return bossName;
    }
    const std::set<Day> getWorkingDays() const{
        return workingDays;
    }
};

class Register {
private:
    std::vector<Record*> records;
    std::map<std::string, std::vector<Record*>> nameIndex;
    std::map<std::string, std::vector<Record*>> departmentIndex;
    std::map<std::string, std::vector<Record*>> SubordinatesIndex;
    std::map<Day, std::vector<Record*>> workDaysIndex;
    long totalRecordNum;


public:
    Register():totalRecordNum(0) {}

    ~Register() {
        for (Record* record : records) {
            delete record;
        }
    }

    void loadFromFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cout << "Failed to open file: " << filename << std::endl;
            return;
        }

        std::string line;
        while (std::getline(file, line)) {
            Record* record = new Record(line);
            totalRecordNum++;
            cout << *record << endl;
            records.push_back(record);
            nameIndex[record->getEmployeeName()].push_back(record);
            departmentIndex[record->getDepartment()].push_back(record);
            SubordinatesIndex[record->getBossName()].push_back(record);
            for(auto day: record->getWorkingDays()){
                workDaysIndex[day].push_back(record);
            }
        }

        file.close();
        cout << "loading complete!" << endl;
    }

    void clear() {
        for (Record* record : records) {
            delete record;
        }

        records.clear();
        nameIndex.clear();
        departmentIndex.clear();
        SubordinatesIndex.clear();
        workDaysIndex.clear();
    }

   long getRecordNum() const {
       return totalRecordNum;
   }
    Register& operator=(Register other) {
        std::swap(records, other.records);
        return *this;
    }

    const std::vector<Record*>& getStorage() const {
        return records;
    }

    const std::vector<Record*>* lookupEmployeeByName(const std::string& name) const {
        auto iter = nameIndex.find(name);
            if (iter != nameIndex.end()) {
                return &(iter->second);
            }
            return nullptr;
    }


    const std::vector<Record*>* lookupEmployeewByDepartment(const std::string& name) const {
        auto iter = departmentIndex.find(name);
            if (iter != departmentIndex.end()) {
                return &(iter->second);
            }
            return nullptr;
    }


    const std::vector<Record*>* getSubordinates(const std::string& name) const {
        auto iter =  SubordinatesIndex.find(name);
        if (iter !=  SubordinatesIndex.end()) {
            return &(iter->second);
        }
         return nullptr;
    }

    const std::vector<Record*>* getEmployeesByWorkingDays(Day workingDays) const {
        auto iter =  workDaysIndex.find(workingDays);
        if (iter !=  workDaysIndex.end()) {
            return &(iter->second);
        }
         return nullptr;
    }
};


// Main program
int main() {
    Register reg;
    cout << "init record num: "<< reg.getRecordNum() << endl;
    std::string fileName= "/Users/aliciaqi/Desktop/learnspace/HSE-Courses/c++/week6/week6_hw/employee.csv";
    reg.loadFromFile(fileName);
    std::vector<Record*> records = reg.getStorage();
    cout << "loaded record num: "<< reg.getRecordNum() << endl;
    for(auto record :*reg.lookupEmployeeByName("Adam Smith") ){
        cout << "--name: "<< *record << endl;
    }

    for(auto record :*reg.getSubordinates("Alice") ){
        cout <<"-- sub:" << *record << endl;
    }

    for(auto record :*reg.getEmployeesByWorkingDays(Day::Mon) ){
        cout <<"-- Day:" << *record << endl;
    }

    return 0;


}
