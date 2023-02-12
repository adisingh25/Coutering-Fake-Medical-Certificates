// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Certificatess
{
    struct Doctor{
        string did;
        string d_name;
    }

    struct Patient{
        string pid;
        string p_name;
        uint adhaar_no;
    }

    struct Certificate{
        string slipno;
        string cid;
        string did;
        string dname;
        string pid;
        string pname;
        string date;
        string address1;
        bool exist;
    }

    mapping(string=>Doctor) public doctors;
    mapping(string=>Patient) public patients;
    mapping(string=>Certificate) public certificates;
    mapping(string=>Certificate) public certificates2;

    function DoctorRegistration(string memory did,string memory d_name) public
    {
        doctors[did]=Doctor(did,d_name);
    }

    function PatientRegistration(string memory pid,string memory p_name,uint adhaar_no) public
    {
        patients[pid]=Patient(pid,p_name,adhaar_no);
    }

    function MedicalCertificate(string memory slipno,string memory cid,string memory did,string memory dname,string memory pid,string memory pname,string memory date,string memory address1) public
    {
        certificates[cid]=Certificate(slipno,cid,did,dname,pid,pname,date,address1,true);
        certificates2[slipno]=Certificate(slipno,cid,did,dname,pid,pname,date,address1,true);
    }

    function Check1(string memory cid) public view returns(string memory)
    {
        bytes memory ccid = bytes(cid);
        if(ccid.length!=0&&certificates[cid].exist==true)
        {
            require(certificates[cid].exist==true);
            return certificates[cid].date;
        }
        else{
            return "0";
        }
    }

    function Check2(string memory cid) public view returns(string memory)
    {
        bytes memory ccid = bytes(cid);
        if(ccid.length!=0&&certificates[cid].exist==true)
        {
            require(certificates[cid].exist==true);
            return certificates[cid].pname;
        }
        else{
            return "0";
        }
    }
    
    function Check3(string memory slipno) public view returns(string memory)
    {
        bytes memory ccid = bytes(slipno);
        if(ccid.length!=0&&certificates2[slipno].exist==true)
        {
            require(certificates2[slipno].exist==true);
            return certificates2[slipno].cid;
        }
        else{
            return "0";
        }
    }

}