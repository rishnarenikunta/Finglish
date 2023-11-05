import React, { useState } from "react";
import { BsUpload } from "react-icons/bs";
import { TiDelete } from "react-icons/ti";
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

function Document() {

    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (e) => {
        console.log(e);
        console.log(e.target.files[0]);
        //send file to backend
        setSelectedFile(e.target.files[0]);

        // const params = {
        //     file: selectedFile
        // };=-

        // HTMLOutputElement(params)
    };


    return (
        <>
            <div className="top">
                <label htmlFor="file-upload" className="custom-file-upload">
                    Browse
                </label>
                <input id="file-upload" type="file" onChange={handleFileChange} />
            </div>
            <div className="bodyDocument">
                <div className="reworded">
                    <div className="specificReword">
                        Hello
                        <div className="regenerate">
                            Generate Again
                        </div>
                    </div>
                    <div className="specificReword">
                        Hello
                    </div>
                </div>
                <div className="doc">
                    <div className="section">
                        Exhibit 10.17 Automobile Lease Agreement between Better Solutions, Inc. and BMW Financial Services BMW Financial Services Motor Vehicle Agreement (Closed End) 1. Parties Lessor Name and Address Lessee and Co-Lessee Name and Address A AND L MOTOR SALES BETTER SOLUTIONS INC. 3780 WILLIAM PENN HIGHWAY 200 PENN CENTER SUITE 201 MONROEVILLE PA 15146 PITTSBURGH PA 15235 2. Agreement to Lease. This Motor Vehicle Lease Agreement ("Lease") is entered into between the lessee and co-lessee
                    </div>
                    <div className="section">
                        Exhibit 10.17 Automobile Lease Agreement between Better Solutions, Inc. and BMW Financial Services BMW Financial Services Motor Vehicle Agreement (Closed End) 1. Parties Lessor Name and Address Lessee and Co-Lessee Name and Address A AND L MOTOR SALES BETTER SOLUTIONS INC. 3780 WILLIAM PENN HIGHWAY 200 PENN CENTER SUITE 201 MONROEVILLE PA 15146 PITTSBURGH PA 15235 2. Agreement to Lease. This Motor Vehicle Lease Agreement ("Lease") is entered into between the lessee and co-lessee
                    </div>
                </div>
            </div>
        </>
    )
}

export default Document;