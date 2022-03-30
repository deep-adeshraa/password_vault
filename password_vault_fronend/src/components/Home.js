import { useEffect, useState } from "react";
import API_CLIENT from "../api/axiosClient";
import { Card } from "react-bootstrap";
import { Fragment } from "react/cjs/react.production.min";
import SideBar from "./SideBar";
import PasswordVault from "./PasswordVault";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import 'react-quill/dist/quill.snow.css';
import { Button, Modal } from 'react-bootstrap';
import Input from "./common/Input";
import PasswordVaultEdit from "./PasswordVaultEdit";


function Home() {
	const [modalShow, setModalShow] = useState(false);
	const [show, setShow] = useState(false);

	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);

	const [modalShowEdit, setModalShowEdit] = useState(false);
	const [showEdit, setShowEdit] = useState(false);

	const handleCloseEdit = () => setShowEdit(false);
	const handleShowEdit = () => setShowEdit(true);

	const Vaults = [
		{ image_path: "../assets/img/outlook.jpeg", title: "Outlook" },
		{ image_path: "../assets/img/google.png", title: "Google" },
		{ image_path: "../assets/img/linkedin.png", title: "Linkedin" },
		{ image_path: "../assets/img/dalhousie.png", title: "Dalhousie" },
		{ image_path: "../assets/img/netflix.png", title: "Netflix" },
		{ image_path: "../assets/img/amazon.png", title: "Amazon" },
		{ image_path: "../assets/img/facebook.png", title: "Facebook" }
	];


	const renderboostrapCard = (data, index) => {
		return (
			<>
				<div class="col-lg-3 col-md-6 col-sm-6">
					<div class="card card-stats">
						<div class="card-body" onClick={handleShowEdit}>
							<div class="row">
								<div class="col-5 col-md-10">
									<div>
										<img src={data.image_path} class="card-logo"></img>
									</div>
								</div>
							</div>
							<div class="row">
								<div class="col-12 col-md-10">
									<p class="card-title">{data.title}</p>
								</div>
							</div>
							<div class="row">
								<div class="col-5 col-md-10">
									<p class="card-category">{data.user_id}</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</>
		)
	}

	return (<>
		<Modal
			show={show}
			onHide={handleClose}
			backdrop="static"
			keyboard={false}

		>
			<Modal.Header closeButton>
				<Modal.Title>Enter M-PIN</Modal.Title>
			</Modal.Header>
			<Modal.Body>
				<Input type="text" name="m_pin" placeholder="M-PIN" required="true" />
			</Modal.Body>
			<Modal.Footer>
				<Button variant="secondary" onClick={handleClose}>
					Close
				</Button>
				<Button variant="primary" onClick={() => { handleClose(true); setModalShow(true) }}>Submit</Button>
			</Modal.Footer>
		</Modal>
		<PasswordVault
			onHide={handleClose}
			show={modalShow}
			onHide={() => setModalShow(false)}
		/>
		<Modal
			show={showEdit}
			onHide={handleCloseEdit}
			backdrop="static"
			keyboard={false}

		>
			<Modal.Header closeButton>
				<Modal.Title>Enter M-PIN</Modal.Title>
			</Modal.Header>
			<Modal.Body>
				<Input type="text" name="m_pin" placeholder="M-PIN" required="true" />
			</Modal.Body>
			<Modal.Footer>
				<Button variant="secondary" onClick={handleCloseEdit}>
					Close
				</Button>
				<Button variant="primary" onClick={() => { handleCloseEdit(true); setModalShowEdit(true) }}>Submit</Button>
			</Modal.Footer>
		</Modal>
		<PasswordVaultEdit
			onHide={handleCloseEdit}
			show={modalShowEdit}
			onHide={() => setModalShowEdit(false)}
		/>

		<Fragment>
			<div class="wrapper ">
				<SideBar />
				<div class="main-panel">
					<nav class="navbar navbar-expand-lg navbar-absolute fixed-top navbar-transparent">
						<div class="container-fluid">
							<div class="navbar-wrapper">
								<div class="navbar-toggle">
									<button type="button" class="navbar-toggler">
										<span class="navbar-toggler-bar bar1"></span>
										<span class="navbar-toggler-bar bar2"></span>
										<span class="navbar-toggler-bar bar3"></span>
									</button>
								</div>
								<a class="navbar-brand" href="javascript:;">Password Vault  {show ? null : <FontAwesomeIcon className='ms-2' data-tip="Click to add new password" onClick={handleShow} icon="fa-solid fa-plus" />}</a>
							</div>

							<div class="collapse navbar-collapse justify-content-end" id="navigation">
								<form>
									<div class="input-group no-border">
										<input type="text" value="" class="form-control" placeholder="Search..." />
										<div class="input-group-append">
											<div class="input-group-text">
												<i class="nc-icon nc-zoom-split"></i>
											</div>
										</div>
									</div>
								</form>
							</div>
						</div>
					</nav>

					<div class="content">
						<div class="row">
							{Vaults.map(renderboostrapCard)}
						</div>
					</div>
				</div>
			</div>
		</Fragment>
	</>
	)
}


export default Home;
