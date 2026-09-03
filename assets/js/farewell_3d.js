/**
 * ============================================================================
 * FAREWELL 3D WEBGL CINEMATIC ENGINE
 * Persistent Three.js Background Experience with Interactive Story Progression
 * ============================================================================
 */
(function() {
    'use strict';

    // Prevent duplicate initializations
    if (window.__farewell3DInitialized) return;
    window.__farewell3DInitialized = true;

    const pDoc = window.document;
    const isMobile = /Android|iPhone|iPad|iPod|Mobile/i.test(navigator.userAgent) || window.innerWidth < 768;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // ------------------------------------------------------------------------
    // 1. Scene, Camera, and Renderer Setup
    // ------------------------------------------------------------------------
    let scene, camera, renderer, clock;
    let canvas;
    let width = window.innerWidth;
    let height = window.innerHeight;

    let mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    let scrollProgress = { current: 0, target: 0 };
    let activeChapter = 'home';

    // Groups for scene hierarchy
    let worldGroup, landingGroup, chapterGroup;
    let boyGroup, girlGroup, pathGroup, treesGroup, lampsGroup;
    let memoriesGroup, wordsGroup, respectGroup, intentionsGroup, duaGroup, goodbyeGroup;
    let petalsMesh, petalDummy, petalData = [];

    // Lighting references
    let ambientLight, directionalLight, horizonPointLight;
    let streetLampLights = [];

    function init() {
        // Create persistent full-screen canvas
        canvas = pDoc.getElementById('farewell3DCanvas');
        if (!canvas) {
            canvas = pDoc.createElement('canvas');
            canvas.id = 'farewell3DCanvas';
            canvas.style.cssText = 'position:fixed; inset:0; width:100vw; height:100vh; z-index:0; pointer-events:none; background:#090D1B;';
            pDoc.body.prepend(canvas);
        }

        // Clock
        clock = new THREE.Clock();

        // Scene
        scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x090D1B, 0.022);

        // Camera
        camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
        camera.position.set(0, 2.2, 7.5);
        camera.lookAt(0, 1.8, 0);

        // Renderer
        renderer = new THREE.WebGLRenderer({
            canvas: canvas,
            alpha: true,
            antialias: !isMobile,
            powerPreference: 'high-performance'
        });
        renderer.setSize(width, height);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, isMobile ? 1.2 : 2.0));
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.1;

        // Hierarchy Groups
        worldGroup = new THREE.Group();
        landingGroup = new THREE.Group();
        chapterGroup = new THREE.Group();

        worldGroup.add(landingGroup);
        worldGroup.add(chapterGroup);
        scene.add(worldGroup);

        // Build Scene Layers
        setupLighting();
        setupSkyAndMountains();
        setupPromenadeAndRailing();
        setupStreetLamps();
        setupSakuraTrees();
        setupInstancedPetals();
        setupBoyModel();
        setupGirlModel();

        // Setup Chapter-Specific 3D Objects
        setupChapterObjects();

        // Event Listeners
        window.addEventListener('resize', onWindowResize, false);
        window.addEventListener('pointermove', onPointerMove, { passive: true });

        // Bind global bridges
        window.__farewellSet3DChapter = setChapter;
        window.__farewellOnScroll = onScrollUpdate;

        // Start render loop
        animate();
    }

    // ------------------------------------------------------------------------
    // 2. Cinematic Lighting & Sky
    // ------------------------------------------------------------------------
    function setupLighting() {
        ambientLight = new THREE.AmbientLight(0x242036, 0.9);
        scene.add(ambientLight);

        // Warm sunset / twilight directional light
        directionalLight = new THREE.DirectionalLight(0xF5B18F, 1.4);
        directionalLight.position.set(-5, 6, 4);
        scene.add(directionalLight);

        // Soft rose rim light from horizon
        horizonPointLight = new THREE.PointLight(0xE96582, 1.8, 25);
        horizonPointLight.position.set(0, 2.5, -8);
        scene.add(horizonPointLight);
    }

    function setupSkyAndMountains() {
        // Gradient Sky Hemisphere Dome
        const skyGeo = new THREE.SphereGeometry(60, 24, 16);
        const skyMat = new THREE.ShaderMaterial({
            uniforms: {
                topColor: { value: new THREE.Color(0x090D1B) },
                bottomColor: { value: new THREE.Color(0x27192C) },
                offset: { value: 2 },
                exponent: { value: 0.6 }
            },
            vertexShader: `
                varying vec3 vWorldPosition;
                void main() {
                    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
                    vWorldPosition = worldPosition.xyz;
                    gl_Position = projectionMatrix * viewMatrix * worldPosition;
                }
            `,
            fragmentShader: `
                uniform vec3 topColor;
                uniform vec3 bottomColor;
                uniform float offset;
                uniform float exponent;
                varying vec3 vWorldPosition;
                void main() {
                    float h = normalize(vWorldPosition + offset).y;
                    gl_FragColor = vec4(mix(bottomColor, topColor, max(pow(max(h, 0.0), exponent), 0.0)), 1.0);
                }
            `,
            side: THREE.BackSide,
            depthWrite: false
        });
        const skyDome = new THREE.Mesh(skyGeo, skyMat);
        scene.add(skyDome);

        // Distant Mountain Ridges
        const mountainGeo = new THREE.PlaneGeometry(80, 16, 32, 8);
        const pos = mountainGeo.attributes.position;
        for (let i = 0; i < pos.count; i++) {
            const px = pos.getX(i);
            const py = pos.getY(i);
            if (py > -6) {
                pos.setZ(i, Math.sin(px * 0.18) * 2.2 + Math.cos(px * 0.4) * 1.1);
            }
        }
        mountainGeo.computeVertexNormals();

        const mountainMat = new THREE.MeshStandardMaterial({
            color: 0x121426,
            roughness: 0.95,
            metalness: 0.05
        });
        const mountains = new THREE.Mesh(mountainGeo, mountainMat);
        mountains.position.set(0, 4, -28);
        scene.add(mountains);

        // Crescent Moon in the sky
        const moonGroup = new THREE.Group();
        const moonGeo = new THREE.RingGeometry(1.2, 1.6, 32, 1, 0, Math.PI * 1.25);
        const moonMat = new THREE.MeshBasicMaterial({
            color: 0xFFF0E0,
            side: THREE.DoubleSide
        });
        const moonMesh = new THREE.Mesh(moonGeo, moonMat);
        moonMesh.rotation.z = 0.4;
        moonGroup.add(moonMesh);

        // Soft Moon Glow
        const moonGlowGeo = new THREE.CircleGeometry(1.8, 24);
        const moonGlowMat = new THREE.MeshBasicMaterial({
            color: 0xF3B086,
            transparent: true,
            opacity: 0.22
        });
        const moonGlow = new THREE.Mesh(moonGlowGeo, moonGlowMat);
        moonGroup.add(moonGlow);

        moonGroup.position.set(9, 12, -26);
        scene.add(moonGroup);
    }

    // ------------------------------------------------------------------------
    // 3. Promenade Walkway & Railing
    // ------------------------------------------------------------------------
    function setupPromenadeAndRailing() {
        pathGroup = new THREE.Group();

        // Brick Promenade Ground
        const groundGeo = new THREE.PlaneGeometry(16, 60, 24, 60);
        const groundMat = new THREE.MeshStandardMaterial({
            color: 0x18172B,
            roughness: 0.75,
            metalness: 0.15
        });
        const ground = new THREE.Mesh(groundGeo, groundMat);
        ground.rotation.x = -Math.PI / 2;
        ground.position.set(1.5, 0, -15);
        pathGroup.add(ground);

        // Promenade Edge Curb
        const curbGeo = new THREE.BoxGeometry(0.5, 0.35, 60);
        const curbMat = new THREE.MeshStandardMaterial({ color: 0x242036, roughness: 0.6 });
        const curb = new THREE.Mesh(curbGeo, curbMat);
        curb.position.set(4.5, 0.17, -15);
        pathGroup.add(curb);

        // Iron Promenade Railing along the right side
        const railMat = new THREE.MeshStandardMaterial({
            color: 0x302436,
            roughness: 0.4,
            metalness: 0.8
        });

        // Top Rail Bar
        const topRailGeo = new THREE.CylinderGeometry(0.04, 0.04, 60, 8);
        const topRail = new THREE.Mesh(topRailGeo, railMat);
        topRail.rotation.x = Math.PI / 2;
        topRail.position.set(4.5, 1.15, -15);
        pathGroup.add(topRail);

        // Bottom Rail Bar
        const botRail = topRail.clone();
        botRail.position.set(4.5, 0.45, -15);
        pathGroup.add(botRail);

        // Vertical Rail Posts
        const postGeo = new THREE.CylinderGeometry(0.03, 0.03, 1.1, 6);
        for (let z = 5; z > -40; z -= 1.6) {
            const post = new THREE.Mesh(postGeo, railMat);
            post.position.set(4.5, 0.55, z);
            pathGroup.add(post);
        }

        landingGroup.add(pathGroup);
    }

    // ------------------------------------------------------------------------
    // 4. Glowing Victorian Street Lamps
    // ------------------------------------------------------------------------
    function setupStreetLamps() {
        lampsGroup = new THREE.Group();
        streetLampLights = [];

        const lampPositions = [
            { x: 3.8, z: 2.0 },
            { x: 3.5, z: -5.5 },
            { x: 3.2, z: -13.0 },
            { x: 2.9, z: -20.5 },
            { x: 2.6, z: -28.0 }
        ];

        const poleMat = new THREE.MeshStandardMaterial({ color: 0x1f1d2c, metalness: 0.85, roughness: 0.3 });
        const lampGlowMat = new THREE.MeshBasicMaterial({ color: 0xFFDFBA });

        lampPositions.forEach((pos, idx) => {
            const lampObj = new THREE.Group();

            // Pole
            const poleGeo = new THREE.CylinderGeometry(0.06, 0.09, 3.2, 8);
            const pole = new THREE.Mesh(poleGeo, poleMat);
            pole.position.y = 1.6;
            lampObj.add(pole);

            // Lamp Arm & Cap
            const capGeo = new THREE.ConeGeometry(0.35, 0.3, 6);
            const cap = new THREE.Mesh(capGeo, poleMat);
            cap.position.y = 3.35;
            lampObj.add(cap);

            // Glowing Lantern Glass
            const lanternGeo = new THREE.CylinderGeometry(0.2, 0.14, 0.35, 6);
            const lantern = new THREE.Mesh(lanternGeo, lampGlowMat);
            lantern.position.y = 3.1;
            lampObj.add(lantern);

            // Soft Volumetric Warm Point Light
            const light = new THREE.PointLight(0xEAB378, 1.6, 9.5, 1.8);
            light.position.y = 3.1;
            lampObj.add(light);
            streetLampLights.push(light);

            lampObj.position.set(pos.x, 0, pos.z);
            lampsGroup.add(lampObj);
        });

        landingGroup.add(lampsGroup);
    }

    // ------------------------------------------------------------------------
    // 5. Stylized Sakura (Cherry Blossom) Trees
    // ------------------------------------------------------------------------
    function setupSakuraTrees() {
        treesGroup = new THREE.Group();

        const trunkMat = new THREE.MeshStandardMaterial({ color: 0x2A1B22, roughness: 0.9 });
        const foliageMat = new THREE.MeshStandardMaterial({
            color: 0xF39AA7,
            roughness: 0.6,
            metalness: 0.1,
            emissive: 0xDF5E7A,
            emissiveIntensity: 0.12
        });

        const treePositions = [
            { x: -3.8, z: 1.0, scale: 1.1 },
            { x: -4.2, z: -7.0, scale: 0.95 },
            { x: -3.5, z: -15.0, scale: 0.85 },
            { x: -3.9, z: -23.0, scale: 0.75 },
            { x: 5.8, z: -3.0, scale: 1.0 },
            { x: 5.2, z: -18.0, scale: 0.8 }
        ];

        treePositions.forEach(tp => {
            const tree = new THREE.Group();

            // Trunk
            const trunkGeo = new THREE.CylinderGeometry(0.12 * tp.scale, 0.22 * tp.scale, 3.5 * tp.scale, 8);
            const trunk = new THREE.Mesh(trunkGeo, trunkMat);
            trunk.position.y = (3.5 * tp.scale) / 2;
            trunk.rotation.z = (Math.random() - 0.5) * 0.15;
            tree.add(trunk);

            // Foliage Clusters
            const clusterCount = 5;
            for (let c = 0; c < clusterCount; c++) {
                const fSize = (0.8 + Math.random() * 0.7) * tp.scale;
                const fGeo = new THREE.DodecahedronGeometry(fSize, 1);
                const foliage = new THREE.Mesh(fGeo, foliageMat);
                foliage.position.set(
                    (Math.random() - 0.5) * 1.5 * tp.scale,
                    (2.8 + Math.random() * 1.2) * tp.scale,
                    (Math.random() - 0.5) * 1.5 * tp.scale
                );
                tree.add(foliage);
            }

            tree.position.set(tp.x, 0, tp.z);
            treesGroup.add(tree);
        });

        landingGroup.add(treesGroup);
    }

    // ------------------------------------------------------------------------
    // 6. Instanced Realistic Floating Cherry Blossom Petals
    // ------------------------------------------------------------------------
    function setupInstancedPetals() {
        const petalCount = isMobile ? 180 : 450;

        // Custom Petal Curved Geometry
        const shape = new THREE.Shape();
        shape.moveTo(0, 0);
        shape.bezierCurveTo(0.08, 0.08, 0.14, 0.2, 0, 0.32);
        shape.bezierCurveTo(-0.14, 0.2, -0.08, 0.08, 0, 0);

        const petalGeo = new THREE.ShapeGeometry(shape, 6);
        const petalMat = new THREE.MeshStandardMaterial({
            color: 0xF8EDE4,
            emissive: 0xE96582,
            emissiveIntensity: 0.25,
            side: THREE.DoubleSide,
            roughness: 0.5,
            metalness: 0.1,
            transparent: true,
            opacity: 0.92
        });

        petalsMesh = new THREE.InstancedMesh(petalGeo, petalMat, petalCount);
        petalDummy = new THREE.Object3D();
        petalData = [];

        for (let i = 0; i < petalCount; i++) {
            const data = {
                x: (Math.random() - 0.5) * 18,
                y: 0.2 + Math.random() * 7.5,
                z: -30 + Math.random() * 38,
                vx: -0.015 - Math.random() * 0.02,
                vy: -0.008 - Math.random() * 0.012,
                vz: 0.005 + Math.random() * 0.01,
                rotX: Math.random() * Math.PI * 2,
                rotY: Math.random() * Math.PI * 2,
                rotZ: Math.random() * Math.PI * 2,
                rotSpeedX: (Math.random() - 0.5) * 0.04,
                rotSpeedY: (Math.random() - 0.5) * 0.03,
                rotSpeedZ: (Math.random() - 0.5) * 0.04,
                scale: 0.6 + Math.random() * 0.7,
                swaySeed: Math.random() * 100
            };
            petalData.push(data);

            petalDummy.position.set(data.x, data.y, data.z);
            petalDummy.scale.setScalar(data.scale);
            petalDummy.updateMatrix();
            petalsMesh.setMatrixAt(i, petalDummy.matrix);
        }

        petalsMesh.instanceMatrix.needsUpdate = true;
        landingGroup.add(petalsMesh);
    }

    // ------------------------------------------------------------------------
    // 7. Stylized 3D Character Figures: Boy & Girl
    // ------------------------------------------------------------------------
    function setupBoyModel() {
        boyGroup = new THREE.Group();

        const clothesMat = new THREE.MeshStandardMaterial({ color: 0x17162A, roughness: 0.8 });
        const skinMat = new THREE.MeshStandardMaterial({ color: 0xF3E2DA, roughness: 0.6 });
        const hairMat = new THREE.MeshStandardMaterial({ color: 0x201A24, roughness: 0.9 });

        // Torso / Dark Hoodie
        const torsoGeo = new THREE.CylinderGeometry(0.24, 0.28, 0.85, 10);
        const torso = new THREE.Mesh(torsoGeo, clothesMat);
        torso.position.y = 1.35;
        boyGroup.add(torso);

        // Legs / Pants
        const legGeo = new THREE.CylinderGeometry(0.1, 0.09, 0.95, 8);
        const leftLeg = new THREE.Mesh(legGeo, clothesMat);
        leftLeg.position.set(-0.12, 0.5, 0);
        boyGroup.add(leftLeg);

        const rightLeg = new THREE.Mesh(legGeo, clothesMat);
        rightLeg.position.set(0.12, 0.5, 0);
        boyGroup.add(rightLeg);

        // Head
        const headGeo = new THREE.SphereGeometry(0.16, 12, 12);
        const head = new THREE.Mesh(headGeo, skinMat);
        head.position.y = 1.95;
        boyGroup.add(head);

        // Hair
        const hairGeo = new THREE.SphereGeometry(0.18, 10, 10);
        const hair = new THREE.Mesh(hairGeo, hairMat);
        hair.position.set(0, 2.02, -0.02);
        boyGroup.add(hair);

        // Arms resting near railing
        const armGeo = new THREE.CylinderGeometry(0.07, 0.06, 0.7, 8);
        const rightArm = new THREE.Mesh(armGeo, clothesMat);
        rightArm.position.set(0.28, 1.3, 0.15);
        rightArm.rotation.set(-0.5, 0.2, -0.3);
        boyGroup.add(rightArm);

        // Boy position: Foreground right near railing looking forward-left
        boyGroup.position.set(3.6, 0, 3.2);
        boyGroup.rotation.y = -Math.PI * 0.72;
        landingGroup.add(boyGroup);
    }

    function setupGirlModel() {
        girlGroup = new THREE.Group();

        const coatMat = new THREE.MeshStandardMaterial({ color: 0x4A2A38, roughness: 0.7 });
        const skirtMat = new THREE.MeshStandardMaterial({ color: 0xF3E2DA, roughness: 0.6 });
        const skinMat = new THREE.MeshStandardMaterial({ color: 0xF8EDE4, roughness: 0.5 });
        const hairMat = new THREE.MeshStandardMaterial({ color: 0x362128, roughness: 0.8 });
        const suitcaseMat = new THREE.MeshStandardMaterial({
            color: 0xE96582,
            roughness: 0.4,
            metalness: 0.3
        });

        // Torso / Overcoat
        const torsoGeo = new THREE.CylinderGeometry(0.18, 0.26, 0.75, 10);
        const torso = new THREE.Mesh(torsoGeo, coatMat);
        torso.position.y = 1.25;
        girlGroup.add(torso);

        // Skirt
        const skirtGeo = new THREE.ConeGeometry(0.32, 0.5, 10);
        const skirt = new THREE.Mesh(skirtGeo, skirtMat);
        skirt.position.y = 0.75;
        girlGroup.add(skirt);

        // Head
        const headGeo = new THREE.SphereGeometry(0.14, 12, 12);
        const head = new THREE.Mesh(headGeo, skinMat);
        head.position.y = 1.78;
        girlGroup.add(head);

        // Flowing Hair
        const hairGeo = new THREE.CylinderGeometry(0.15, 0.22, 0.55, 8);
        const hair = new THREE.Mesh(hairGeo, hairMat);
        hair.position.set(0, 1.7, -0.06);
        hair.rotation.x = 0.18;
        girlGroup.add(hair);

        // Rose / Coral Suitcase with handle
        const suitcaseBodyGeo = new THREE.BoxGeometry(0.35, 0.45, 0.22);
        const suitcase = new THREE.Mesh(suitcaseBodyGeo, suitcaseMat);
        suitcase.position.set(-0.45, 0.32, 0.1);
        girlGroup.add(suitcase);

        const handleGeo = new THREE.TorusGeometry(0.06, 0.015, 6, 12);
        const handle = new THREE.Mesh(handleGeo, coatMat);
        handle.position.set(-0.45, 0.58, 0.1);
        handle.rotation.x = Math.PI / 2;
        girlGroup.add(handle);

        // Position: Midground walking away along promenade
        girlGroup.position.set(1.6, 0, -3.5);
        girlGroup.rotation.y = 0; // Facing down the path away from viewer
        landingGroup.add(girlGroup);
    }

    // ------------------------------------------------------------------------
    // 8. Chapter-Specific 3D Objects (Memories, Words, Respect, Dua, Finale)
    // ------------------------------------------------------------------------
    function setupChapterObjects() {
        // --- 1. Memories: Floating 3D Polaroid Frames ---
        memoriesGroup = new THREE.Group();
        const polaroidMat = new THREE.MeshStandardMaterial({ color: 0xFDF8F5, roughness: 0.5 });
        const photoMat = new THREE.MeshStandardMaterial({ color: 0x2A2032, roughness: 0.9 });

        for (let p = 0; p < 5; p++) {
            const frameGroup = new THREE.Group();
            const frameGeo = new THREE.BoxGeometry(0.9, 1.1, 0.02);
            const frame = new THREE.Mesh(frameGeo, polaroidMat);
            frameGroup.add(frame);

            const photoGeo = new THREE.PlaneGeometry(0.74, 0.74);
            const photo = new THREE.Mesh(photoGeo, photoMat);
            photo.position.set(0, 0.1, 0.015);
            frameGroup.add(photo);

            const angle = (p / 5) * Math.PI * 2;
            frameGroup.position.set(Math.cos(angle) * 3.2, 1.8 + (p % 2) * 0.4, Math.sin(angle) * 2.0);
            frameGroup.rotation.set((Math.random() - 0.5) * 0.3, (Math.random() - 0.5) * 0.4, (Math.random() - 0.5) * 0.2);
            memoriesGroup.add(frameGroup);
        }
        memoriesGroup.visible = false;
        chapterGroup.add(memoriesGroup);

        // --- 2. Words: 3D Parchment Sheet & Floating Quill Feather ---
        wordsGroup = new THREE.Group();
        const paperGeo = new THREE.PlaneGeometry(1.6, 2.2, 16, 16);
        const paperPos = paperGeo.attributes.position;
        for (let i = 0; i < paperPos.count; i++) {
            const px = paperPos.getX(i);
            const py = paperPos.getY(i);
            paperPos.setZ(i, Math.sin(px * 2) * 0.08 + Math.cos(py * 1.5) * 0.06);
        }
        paperGeo.computeVertexNormals();

        const paperMat = new THREE.MeshStandardMaterial({
            color: 0xF8EDE4,
            roughness: 0.7,
            side: THREE.DoubleSide
        });
        const paperMesh = new THREE.Mesh(paperGeo, paperMat);
        paperMesh.position.set(0, 1.8, 0);
        wordsGroup.add(paperMesh);

        // Quill Feather
        const featherGeo = new THREE.ConeGeometry(0.12, 1.1, 8);
        const featherMat = new THREE.MeshStandardMaterial({ color: 0xF39AA7, roughness: 0.6 });
        const feather = new THREE.Mesh(featherGeo, featherMat);
        feather.position.set(0.9, 2.2, 0.2);
        feather.rotation.set(0.4, 0.2, -0.6);
        wordsGroup.add(feather);

        wordsGroup.visible = false;
        chapterGroup.add(wordsGroup);

        // --- 3. Respect: Golden Radiant Crystal Star / Lotus ---
        respectGroup = new THREE.Group();
        const crystalGeo = new THREE.OctahedronGeometry(1.1, 1);
        const crystalMat = new THREE.MeshStandardMaterial({
            color: 0xEAB378,
            emissive: 0xEAB378,
            emissiveIntensity: 0.4,
            metalness: 0.8,
            roughness: 0.2,
            wireframe: false
        });
        const crystal = new THREE.Mesh(crystalGeo, crystalMat);
        crystal.position.set(0, 2.0, 0);
        respectGroup.add(crystal);

        const crystalLight = new THREE.PointLight(0xEAB378, 2.2, 8);
        crystalLight.position.set(0, 2.0, 0);
        respectGroup.add(crystalLight);

        respectGroup.visible = false;
        chapterGroup.add(respectGroup);

        // --- 4. Intentions: Translucent Glass Heart ---
        intentionsGroup = new THREE.Group();
        const heartShape = new THREE.Shape();
        heartShape.moveTo(0, 0.4);
        heartShape.bezierCurveTo(0, 0.8, -0.7, 0.8, -0.7, 0.35);
        heartShape.bezierCurveTo(-0.7, 0, 0, -0.6, 0, -0.9);
        heartShape.bezierCurveTo(0, -0.6, 0.7, 0, 0.7, 0.35);
        heartShape.bezierCurveTo(0.7, 0.8, 0, 0.8, 0, 0.4);

        const heartGeo = new THREE.ExtrudeGeometry(heartShape, { depth: 0.3, bevelEnabled: true, bevelSegments: 6, steps: 2, bevelSize: 0.1, bevelThickness: 0.1 });
        const glassMat = new THREE.MeshPhysicalMaterial({
            color: 0xFFCAD4,
            transmission: 0.9,
            opacity: 1,
            transparent: true,
            roughness: 0.1,
            ior: 1.45,
            thickness: 0.8,
            emissive: 0xE96582,
            emissiveIntensity: 0.2
        });
        const heartMesh = new THREE.Mesh(heartGeo, glassMat);
        heartMesh.scale.setScalar(1.2);
        heartMesh.rotation.z = Math.PI;
        heartMesh.position.set(0, 2.2, 0);
        intentionsGroup.add(heartMesh);

        intentionsGroup.visible = false;
        chapterGroup.add(intentionsGroup);

        // --- 5. Dua: Serene Moonlit Sky & Ascending Particles ---
        duaGroup = new THREE.Group();
        const duaCrescentGeo = new THREE.TorusGeometry(1.2, 0.15, 12, 32, Math.PI * 1.3);
        const duaMoonMat = new THREE.MeshStandardMaterial({
            color: 0xFFF8ED,
            emissive: 0xFFF0E0,
            emissiveIntensity: 0.6
        });
        const duaMoon = new THREE.Mesh(duaCrescentGeo, duaMoonMat);
        duaMoon.position.set(0, 2.2, 0);
        duaMoon.rotation.z = 0.5;
        duaGroup.add(duaMoon);

        duaGroup.visible = false;
        chapterGroup.add(duaGroup);

        // --- 6. Final Note: 3D Sealed Farewell Envelope ---
        goodbyeGroup = new THREE.Group();
        const envGeo = new THREE.BoxGeometry(1.8, 1.2, 0.08);
        const envMat = new THREE.MeshStandardMaterial({ color: 0xF8EDE4, roughness: 0.6 });
        const envelope = new THREE.Mesh(envGeo, envMat);
        envelope.position.set(0, 2.0, 0);
        goodbyeGroup.add(envelope);

        const sealGeo = new THREE.CylinderGeometry(0.18, 0.18, 0.04, 16);
        const sealMat = new THREE.MeshStandardMaterial({ color: 0xDF5E7A, roughness: 0.3, metalness: 0.4 });
        const seal = new THREE.Mesh(sealGeo, sealMat);
        seal.rotation.x = Math.PI / 2;
        seal.position.set(0, 2.0, 0.06);
        goodbyeGroup.add(seal);

        goodbyeGroup.visible = false;
        chapterGroup.add(goodbyeGroup);
    }

    // ------------------------------------------------------------------------
    // 9. Chapter Morphing Controller
    // ------------------------------------------------------------------------
    function setChapter(chapId) {
        if (!chapId) return;
        activeChapter = chapId;

        const allGroups = [
            { id: 'home', grp: landingGroup },
            { id: 'welcome', grp: landingGroup },
            { id: 'memories', grp: memoriesGroup },
            { id: 'words', grp: wordsGroup },
            { id: 'respect', grp: respectGroup },
            { id: 'intentions', grp: intentionsGroup },
            { id: 'dua', grp: duaGroup },
            { id: 'goodbye', grp: goodbyeGroup }
        ];

        allGroups.forEach(item => {
            if (item.grp && item.grp !== landingGroup) {
                item.grp.visible = (item.id === chapId);
            }
        });

        if (chapId === 'home' || chapId === 'welcome') {
            landingGroup.visible = true;
        } else {
            // Keep background promenade softly visible behind special objects
            landingGroup.visible = true;
        }
    }

    // ------------------------------------------------------------------------
    // 10. Mouse Parallax & Scroll Handlers
    // ------------------------------------------------------------------------
    function onPointerMove(e) {
        if (prefersReducedMotion) return;
        // Normalize mouse coordinates from -1 to 1
        mouse.targetX = (e.clientX / width - 0.5) * 2;
        mouse.targetY = (e.clientY / height - 0.5) * 2;
    }

    function onScrollUpdate(prog) {
        scrollProgress.target = Math.max(0, Math.min(1, prog));
    }

    function updateCameraFraming() {
        width = window.innerWidth;
        height = window.innerHeight;
        const aspect = width / height;
        camera.aspect = aspect;

        if (aspect < 1.0) {
            // Mobile Portrait (Aspect ~0.45 - 0.75): Frame boy and girl centrally
            camera.fov = 58;
            camera.position.x = 1.3 + mouse.x * 0.2;
            camera.position.y = 2.1 + mouse.y * -0.15 - scrollProgress.current * 0.3;
            camera.position.z = 8.5 - scrollProgress.current * 1.5;
            camera.lookAt(1.6 + mouse.x * 0.08, 1.7 - scrollProgress.current * 0.2, 0);
        } else {
            // Desktop / Landscape
            camera.fov = 45;
            camera.position.x = mouse.x * 0.35;
            camera.position.y = 2.2 + mouse.y * -0.25 - scrollProgress.current * 0.3;
            camera.position.z = 7.5 - scrollProgress.current * 1.5;
            camera.lookAt(mouse.x * 0.1, 1.8 - scrollProgress.current * 0.2, 0);
        }
        camera.updateProjectionMatrix();
        renderer.setSize(width, height);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, width < 768 ? 1.25 : 2.0));
    }

    function onWindowResize() {
        updateCameraFraming();
    }

    // ------------------------------------------------------------------------
    // 11. Animation Loop & Physics
    // ------------------------------------------------------------------------
    function animate() {
        requestAnimationFrame(animate);

        const delta = clock.getDelta();
        const time = clock.getElapsedTime();

        // 1. Smooth Mouse Parallax Dampening (Subtle & Elegant)
        const lerpFactor = 0.04;
        mouse.x += (mouse.targetX - mouse.x) * lerpFactor;
        mouse.y += (mouse.targetY - mouse.y) * lerpFactor;

        // 2. Smooth Scroll Dampening
        scrollProgress.current += (scrollProgress.target - scrollProgress.current) * 0.05;
        const sp = scrollProgress.current;

        // 3. Responsive Camera Position: Parallax + Scroll Transition
        const aspect = width / height;
        if (aspect < 1.0) {
            camera.position.x = 1.3 + mouse.x * 0.2;
            camera.position.y = 2.1 + mouse.y * -0.15 - sp * 0.3;
            camera.position.z = 8.5 - sp * 1.5;
            camera.lookAt(1.6 + mouse.x * 0.08, 1.7 - sp * 0.2, 0);
        } else {
            camera.position.x = mouse.x * 0.35;
            camera.position.y = 2.2 + mouse.y * -0.25 - sp * 0.3;
            camera.position.z = 7.5 - sp * 1.5;
            camera.lookAt(mouse.x * 0.1, 1.8 - sp * 0.2, 0);
        }

        // 4. Girl Character Progression: Slowly walks away down the path as user scrolls
        if (girlGroup) {
            // Base walk position plus scroll advance
            const baseZ = -3.5 - sp * 12.0;
            girlGroup.position.z = baseZ;
            girlGroup.position.x = 1.6 - sp * 0.6; // Moves slightly inward on path

            // Subtle walking bob / hair wind sway
            girlGroup.position.y = Math.abs(Math.sin(time * 3.5 + sp * 20)) * 0.04;
            girlGroup.rotation.z = Math.sin(time * 3.5) * 0.02;
        }

        // 5. Boy Character: Stationary foreground with gentle breathing idle
        if (boyGroup) {
            boyGroup.position.y = Math.sin(time * 1.2) * 0.015;
        }

        // 6. Street Lamps Glow Prominence based on Scroll
        if (streetLampLights.length > 0) {
            const lampIntensity = 1.4 + sp * 0.8 + Math.sin(time * 2.0) * 0.08;
            streetLampLights.forEach(l => {
                l.intensity = lampIntensity;
            });
        }

        // 7. Instanced Floating Cherry Blossom Petals Physics
        if (petalsMesh && petalDummy) {
            const windSpeed = 1.0 + sp * 0.8;
            for (let i = 0; i < petalData.length; i++) {
                const p = petalData[i];

                p.x += (p.vx + Math.sin(time * 0.8 + p.swaySeed) * 0.008) * windSpeed;
                p.y += (p.vy + Math.cos(time * 1.1 + p.swaySeed) * 0.004) * windSpeed;
                p.z += p.vz * windSpeed;

                p.rotX += p.rotSpeedX;
                p.rotY += p.rotSpeedY;
                p.rotZ += p.rotSpeedZ;

                // Reset when out of view
                if (p.y < -0.2 || p.x < -10 || p.z > 10) {
                    p.x = 8 + Math.random() * 4;
                    p.y = 4.5 + Math.random() * 3.5;
                    p.z = -30 + Math.random() * 25;
                }

                petalDummy.position.set(p.x, p.y, p.z);
                petalDummy.rotation.set(p.rotX, p.rotY, p.rotZ);
                petalDummy.scale.setScalar(p.scale);
                petalDummy.updateMatrix();
                petalsMesh.setMatrixAt(i, petalDummy.matrix);
            }
            petalsMesh.instanceMatrix.needsUpdate = true;
        }

        // 8. Rotate Chapter-Specific 3D Artifacts
        if (activeChapter === 'respect' && respectGroup) {
            respectGroup.rotation.y = time * 0.35;
            respectGroup.position.y = Math.sin(time * 1.5) * 0.08;
        } else if (activeChapter === 'intentions' && intentionsGroup) {
            intentionsGroup.rotation.y = Math.sin(time * 0.8) * 0.3;
            intentionsGroup.position.y = Math.sin(time * 1.2) * 0.06;
        } else if (activeChapter === 'memories' && memoriesGroup) {
            memoriesGroup.rotation.y = time * 0.08;
        } else if (activeChapter === 'words' && wordsGroup) {
            wordsGroup.rotation.y = Math.sin(time * 0.6) * 0.15;
            wordsGroup.position.y = Math.sin(time * 1.0) * 0.05;
        } else if (activeChapter === 'dua' && duaGroup) {
            duaGroup.rotation.y = Math.sin(time * 0.4) * 0.12;
        } else if (activeChapter === 'goodbye' && goodbyeGroup) {
            goodbyeGroup.rotation.y = Math.sin(time * 0.5) * 0.2;
            goodbyeGroup.position.y = Math.sin(time * 0.9) * 0.05;
        }

        renderer.render(scene, camera);
    }

    // Auto-initialize when Three.js is ready
    if (window.THREE) {
        init();
    } else {
        const checkThree = setInterval(() => {
            if (window.THREE) {
                clearInterval(checkThree);
                init();
            }
        }, 50);
    }
})();
